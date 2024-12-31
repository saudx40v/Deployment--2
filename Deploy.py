# Function to read logs from a file
def read_logs(file_path):
    try:
        with open(file_path, 'r') as file:
            logs = file.readlines()
        return logs
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return []
    except Exception as e:
        print(f"Error: An unexpected error occurred: {e}")
        return []

# Function to review the logs and categorize them by success or failure
def review_logs(logs):
    successful_logins = []
    failed_logins = []

    # Process each log entry
    for log in logs:
        # Split the log entry into components (user, timestamp, IP, status)
        try:
            user, timestamp, ip, status = log.strip().split(',')
            if status == 'success':
                successful_logins.append((user, timestamp, ip))
            elif status == 'failed':
                failed_logins.append((user, timestamp, ip))
            else:
                print(f"Warning: Invalid status '{status}' in log entry: {log}")
        except ValueError:
            print(f"Warning: Invalid log format in entry: {log}")
            continue

    return successful_logins, failed_logins

# Function to print the results of the log review
def print_review(successful_logins, failed_logins):
    print("Successful Login Attempts:")
    for login in successful_logins:
        print(f"User: {login[0]}, Time: {login[1]}, IP Address: {login[2]}")
    
    print("\nFailed Login Attempts:")
    for login in failed_logins:
        print(f"User: {login[0]}, Time: {login[1]}, IP Address: {login[2]}")

# Main function to execute the log review process
def main():
    file_path = 'login_logs.txt'  # Path to the log file
    logs = read_logs(file_path)  # Read logs from the file
    
    if logs:
        successful_logins, failed_logins = review_logs(logs)  # Review the logs
        print_review(successful_logins, failed_logins)  # Print the results

# Run the program
if __name__ == "__main__":
    main()
