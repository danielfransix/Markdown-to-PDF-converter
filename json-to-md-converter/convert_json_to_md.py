import json
import os

def extract_value(var_data):
    if not isinstance(var_data, dict):
        return str(var_data)
    
    val = var_data.get("$value", "")
    if val == "" and "$alias" in var_data:
        return f"Alias: {var_data['$alias']}"
    return str(val)

def walk(node, path_components):
    tables = []
    
    # Identify variables and subgroups in the current node
    variables = {}
    subgroups = {}
    
    # Sort keys to ensure deterministic output order
    keys = sorted(node.keys())
    
    for key in keys:
        value = node[key]
        if key.startswith("$"):
            continue
            
        is_variable = False
        is_group = False
        
        if isinstance(value, dict):
            if "$value" in value or "$type" in value:
                is_variable = True
            
            # Check if it has children that are not metadata
            has_children = any(not k.startswith("$") for k in value.keys())
            if has_children:
                is_group = True
        
        if is_variable:
            variables[key] = value
        
        if is_group:
            subgroups[key] = value

    # If we have variables at this level, create a table
    if variables:
        table_rows = []
        for name, data in variables.items():
            val = extract_value(data)
            table_rows.append((name, val))
            
        tables.append({
            "title": " / ".join(path_components),
            "rows": table_rows
        })
    
    # Recurse into subgroups
    for name, data in subgroups.items():
        new_path = path_components + [name]
        tables.extend(walk(data, new_path))
        
    return tables

def json_to_markdown(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Access the relevant data structure
    try:
        if isinstance(data, list):
            modes = data[0].get("TailwindCSS", {}).get("modes", {}).get("Default", {})
        else:
            modes = data.get("TailwindCSS", {}).get("modes", {}).get("Default", {})
    except (IndexError, AttributeError):
        print("Error: unexpected JSON structure.")
        return

    all_tables = walk(modes, [])
    
    markdown_lines = []
    for table in all_tables:
        title = table["title"]
        rows = table["rows"]
        
        # Skip empty title if root has no variables (usually root doesn't)
        if not title:
            # If root had variables, we'd label it Root, but unlikely here.
            # If it happens, let's just header it.
            if rows:
                markdown_lines.append("### Root Variables\n")
        else:
            markdown_lines.append(f"### {title}\n")
        
        if rows:
            markdown_lines.append("| Name | Default |")
            markdown_lines.append("| :--- | :--- |")
            
            for name, val in rows:
                markdown_lines.append(f"| {name} | {val} |")
            
            markdown_lines.append("") # Empty line
        
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("\n".join(markdown_lines))
    
    print(f"Successfully created {output_file}")

if __name__ == "__main__":
    json_to_markdown("ys-variables.json", "variables.md")
