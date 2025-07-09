import os
import json
import getpass
from colorama import init, Fore, Style

init(autoreset=True)

CONFIG_FILE = "config.json"

def print_banner():
    print(f"{Fore.CYAN}======================================")
    print(f"{Fore.CYAN}       TGVCMusic Bot Setup")
    print(f"{Fore.CYAN}======================================")
    print(f"{Fore.YELLOW}This script will help you set up your Telegram Voice Chat Music Bot.")
    print(f"{Fore.YELLOW}You'll need the following information:")
    print(f"{Fore.YELLOW}1. Telegram API ID and Hash (from https://my.telegram.org/apps)")
    print(f"{Fore.YELLOW}2. Bot Token (from @BotFather)")
    print(f"{Fore.YELLOW}3. Admin usernames/IDs")
    print(f"{Fore.YELLOW}4. MongoDB URI (optional)")
    print(f"{Fore.CYAN}======================================\n")

def get_input(prompt, is_password=False, required=True, validator=None):
    while True:
        if is_password:
            value = getpass.getpass(prompt)
        else:
            value = input(prompt)
        
        if not value and required:
            print(f"{Fore.RED}This field is required. Please try again.")
            continue
        
        if validator and value:
            if not validator(value):
                continue
        
        return value

def validate_number(value, name):
    try:
        int(value)
        return True
    except ValueError:
        print(f"{Fore.RED}{name} must be a number!")
        return False

def collect_config():
    config = {}
    
    # Get API credentials
    print(f"{Fore.GREEN}Telegram API Credentials:")
    config["api_id"] = get_input("Enter API ID: ", required=True, 
                                validator=lambda x: validate_number(x, "API ID"))
    config["api_hash"] = get_input("Enter API Hash: ", required=True)
    
    # Bot token
    print(f"\n{Fore.GREEN}Bot Information:")
    config["bot_token"] = get_input("Enter Bot Token: ", required=True)
    
    # Session name
    config["session_name"] = get_input("Enter Session Name (default: TGVCMusic): ", required=False) or "TGVCMusic"
    
    # Admin users
    print(f"\n{Fore.GREEN}Admin Configuration:")
    admins = []
    print("Enter admin usernames or IDs (one per line, leave empty to finish):")
    while True:
        admin = get_input("Admin username/ID (or empty to finish): ", required=False)
        if not admin:
            break
        admins.append(admin)
    
    if not admins:
        config["admins"] = ["me"]
        print(f"{Fore.YELLOW}No admins specified, using 'me' as default admin.")
    else:
        config["admins"] = admins
    
    # MongoDB (optional)
    print(f"\n{Fore.GREEN}Database Configuration (Optional):")
    config["use_mongodb"] = get_input("Use MongoDB? (y/n): ", required=False).lower() == "y"
    if config["use_mongodb"]:
        config["mongodb_uri"] = get_input("MongoDB URI: ", required=True)
    
    # Additional settings
    print(f"\n{Fore.GREEN}Additional Settings:")
    config["download_path"] = get_input("Download Path (default: downloads): ", required=False) or "downloads"
    config["duration_limit"] = get_input("Song Duration Limit in Minutes (default: 10): ", required=False) or "10"
    
    return config

def save_config(config):
    try:
        with open(CONFIG_FILE, 'w') as f:
            json.dump(config, f, indent=4)
        
        # Also save as environment file for Docker/Heroku compatibility
        with open('.env', 'w') as f:
            for key, value in config.items():
                if isinstance(value, list):
                    f.write(f"{key.upper()}={','.join(value)}\n")
                else:
                    f.write(f"{key.upper()}={value}\n")
                    
        print(f"{Fore.GREEN}Configuration saved successfully!")
    except Exception as e:
        print(f"{Fore.RED}Error saving configuration: {e}")

def main():
    print_banner()
    
    # Check if config already exists
    if os.path.exists(CONFIG_FILE):
        overwrite = input(f"{Fore.YELLOW}Configuration file already exists. Overwrite? (y/n): ").lower() == "y"
        if not overwrite:
            print(f"{Fore.GREEN}Setup cancelled. Using existing configuration.")
            return
    
    # Collect configuration
    config = collect_config()
    
    # Save configuration
    save_config(config)
    
    print(f"\n{Fore.GREEN}Setup completed successfully!")
    print(f"{Fore.CYAN}You can now run your TGVCMusic bot using: python main.py")

if __name__ == "__main__":
    main()