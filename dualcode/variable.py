import json
import os

def save_variable(variable, name=None):
    """
    Save a variable to variables.json, using its name or a provided name.
    
    Args:
        variable: The variable to save
        name (str, optional): Custom name for the variable. If None, attempts to 
                               use the variable's name in the calling scope.
    """
    # Determine the variable name if not provided
    if name is None:
        # Get the calling frame to inspect variable names
        import inspect
        frame = inspect.currentframe().f_back
        
        # Find the variable name by searching local and global scopes
        var_name = None
        for var, val in {**frame.f_locals, **frame.f_globals}.items():
            if val is variable:
                var_name = var
                break
        
        # If no name found, use a generic name
        name = var_name or 'unnamed_variable'
    
    # Determine file path (saves in the current working directory)
    file_path = os.path.join(os.getcwd(), 'variables.json')
    
    # Read existing data or initialize empty dict
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}
    
    # Save the variable
    data[name] = variable
    
    # Write updated data back to file
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)