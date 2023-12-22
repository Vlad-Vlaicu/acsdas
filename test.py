import time

def test(net):
    # on first server start the listener
    net.get("h1").sendCmd("python3 -m http.server 9000 &")

    num_requests = 100
    
    # Start the client
    net.get("c1").sendCmd("python3 client.py -p http 10.10.101.2:9000 -n {num_requests} &")

    print("Running base test with only one server")
    
    # Wait for the client command to finish and retrieve its output
    output = net.get("c1").waitOutput()
    client_output_lines = output.split('\n')
    for i in range(num_requests):
        print(f"Output for request {i + 1}: {client_output_lines[i]}")

    print("Done")
    print("hint:Quit and check client_log.txt")
    return
