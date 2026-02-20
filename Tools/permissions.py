def check_safety(command: str) -> tuple[bool, str]:
    """
    Analyzes a command for unsafe intent.
    
    Args:
        command (str): The raw user command.
        
    Returns:
        tuple[bool, str]: (is_safe, reason_message)
    """
    command = command.lower()
    
    UNSAFE_KEYWORDS = [
        "delete", "remove", "format", "shutdown", "restart", 
        "uninstall", "wipe", "rm -rf", "kill", "terminate"
    ]
    
    # Check for direct unsafe keywords
    for keyword in UNSAFE_KEYWORDS:
        if keyword in command:
            return False, f"The command contains unsafe actions related to '{keyword}'. Permission denied."
            
    # Allow safe actions
    return True, "Safe"
