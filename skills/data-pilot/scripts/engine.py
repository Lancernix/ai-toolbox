import os
import sys
import argparse
import json

# Add local lib to path for standalone execution
base_dir = os.path.dirname(os.path.abspath(__file__))
lib_path = os.path.join(base_dir, "lib")
if os.path.exists(lib_path):
    sys.path.insert(0, lib_path)

try:
    import polars as pl
except ImportError:
    # Fallback/Error if not installed
    pass

def inspect_file(file_path):
    """Returns headers and inferred types of the file."""
    if file_path.endswith('.xlsx'):
        df = pl.read_excel(file_path, engine="calamine")
    elif file_path.endswith('.parquet'):
        df = pl.read_parquet(file_path)
    else:
        raise ValueError("Unsupported file format. Use .xlsx or .parquet")
    
    schema = {col: str(dtype) for col, dtype in df.schema.items()}
    sample = df.head(5).to_dicts()
    return {"schema": schema, "sample": sample, "rows": df.height}

def upsert_data(source_file, target_parquet, mapping=None):
    """Merges new Excel data into the master Parquet file."""
    df_new = pl.read_excel(source_file, engine="calamine")
    
    if mapping:
        df_new = df_new.rename(mapping)
    
    if os.path.exists(target_parquet):
        df_master = pl.read_parquet(target_parquet)
        df_final = pl.concat([df_master, df_new], how="diagonal")
    else:
        df_final = df_new
        
    df_final.write_parquet(target_parquet)
    return {"status": "success", "total_rows": df_final.height, "added_rows": df_new.height}

def query_data(parquet_path, query_json):
    """Executes an analysis query."""
    df = pl.scan_parquet(parquet_path)
    
    group_by = query_json.get("group_by", [])
    aggs = query_json.get("agg", {})
    
    agg_list = []
    for col, func in aggs.items():
        if func == "sum": agg_list.append(pl.col(col).sum())
        elif func == "mean": agg_list.append(pl.col(col).mean())
        elif func == "count": agg_list.append(pl.col(col).count())
            
    if group_by:
        df = df.group_by(group_by).agg(agg_list)
    else:
        df = df.select(agg_list)
        
    result = df.collect()
    return result.to_dicts()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--action", required=True, choices=["inspect", "upsert", "query"])
    parser.add_argument("--file", help="Source file path")
    parser.add_argument("--target", help="Target Parquet path")
    parser.add_argument("--mapping", help="JSON string for column mapping")
    parser.add_argument("--query", help="JSON string for query parameters")
    
    args = parser.parse_args()
    
    try:
        if args.action == "inspect":
            print(json.dumps(inspect_file(args.file), indent=2))
        elif args.action == "upsert":
            mapping = json.loads(args.mapping) if args.mapping else None
            print(json.dumps(upsert_data(args.file, args.target, mapping), indent=2))
        elif args.action == "query":
            query = json.loads(args.query) if args.query else {}
            print(json.dumps(query_data(args.target, query), indent=2))
    except Exception as e:
        print(json.dumps({"error": str(e)}))
        sys.exit(1)
