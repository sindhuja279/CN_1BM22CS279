def main():
    # Initial packets in the bucket
    storage = 0
    
    # Total number of times bucket content is checked
    no_of_queries = 4
    
    # Total number of packets that can be accommodated in the bucket
    bucket_size = 10
    
    # Number of packets that enter the bucket at a time
    input_pkt_size = 4
    
    # Number of packets that exit the bucket at a time
    output_pkt_size = 1
    
    for _ in range(no_of_queries):
        # Space left in the bucket
        size_left = bucket_size - storage
        
        if input_pkt_size <= size_left:
            # Update storage
            storage += input_pkt_size
        else:
            print(f"Packet loss = {input_pkt_size}")
        
        print(f"Buffer size = {storage} out of bucket size = {bucket_size}")
        
        # Remove packets from storage
        storage -= output_pkt_size

if __name__ == "__main__":
    main()
