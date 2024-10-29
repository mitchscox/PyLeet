import pandas as pd

def parse_message(message):
# TODO We dont take into consideration the first side (the first character?)
    session_letter = message[0]
#   message_type = message[0]
    message_type = message[9]
    message_type_name = 'No message name'
    match message_type:
        case 'E':
            message_type_name = 'Executed Order'
        case 'A':
            message_type_name = 'Add Order'
        case 'P':
            message_type_name = 'Trade Order'
        case 'X':
            message_type_name = 'Cancelled Order'

#    timestamp = message[1:10]
    timestamp = message[1:8]
    order_id = message[10:22]
    side = message[22]
    quantity = message[23:29].strip()  # Leading space padding necessary?
    stock_symbol = message[29:32].strip()  # Strip cause this effects csv creation
    price = message[32:42]
    display = message[42] if len(message) > 42 else None  # Handle cases where display is missing? Check Spec

    return {
        'Session Letter': session_letter,
        'Message Type': message_type,
        'Message Type Name' : message_type_name,
        'Timestamp': timestamp,
        'Order ID': order_id,
        'Side': side,
        'Quantity': quantity,
        #'Quantity': int(quantity) if quantity.isdigit() else 0,
        'Stock Symbol': stock_symbol,
        'Price': price,
        #'Price': float(price) / 10000 if price.isdigit() else 0,
        'Display': display
    }

def process_file(file_path):
    with open(file_path, 'r') as file:
        messages = file.readlines()
    parsed_messages = [parse_message(msg.strip()) for msg in messages]
    df = pd.DataFrame(parsed_messages)
    print(df)
    df.to_csv('parsed_messages.csv', index=False)
    print("Parsed messages saved to 'parsed_messages.csv'.")



process_file('messages.txt')