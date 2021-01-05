address = "change_me"
port = 7744
internet = require("internet")
robot = require("robot")
computer = require("computer")
serialization = require("serialization")


function execute_command(connection)
    local input = connection:read()
    if input ~= nil then
        local command = load(input)
        local return_values = table.pack(command())
        connection:write(serialization.serialize(return_values) .. "\n")
    end
end


function main()
    local connection = internet.open(address, port)
    if (connection) then
        while (true) do
            execute_command(connection)
        end
    end
end


main()
