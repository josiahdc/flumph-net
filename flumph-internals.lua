address = "192.168.1.14"
port = 8181
internet = require("internet")
robot = require("robot")


function main()
    local connection = establish_connection()
    handshake(connection)
    if (connection) then
        while (true) do
            execute_command(connection)
        end
        connection:close()
    end
end


function receive(connection)
    return connection:read()
end


function transmit(connection, message)
    connection:write(message .. "\n")
end


function establish_connection()
    return internet.open(address, port)
end


function handshake(connection)
    print("performing handshake")
    transmit(connection, "flumph")
end


function execute_command(connection)
    print("performing command")
    local input = receive(connection)
    if input ~= nil then
        local command = parse_command_from(input)
        local return_values = table.pack(command())
        transmit(connection, serialize(return_values))
    else
        print("got nil command")
    end
end


function parse_command_from(command_string)
    print("command string is: " .. command_string)
    return load("return " .. command_string)
end

function serialize(return_values)
    local result = ""
    for i = 1, #return_values do
        if i == 1 then
            result = tostring(return_values[i])
        else
            result = result .. "<|>" .. tostring(return_values[i])
        end
    end
    return result
end


main()
