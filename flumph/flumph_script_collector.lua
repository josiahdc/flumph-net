local internet = require("internet")
local thread = require("thread")

local url = "change_me"


function start()
    thread.create(function()
        local response = internet.request(url)
        local file = io.open("/tmp/flumph_script.lua", "w")
        for chunk in response do
            file:write(chunk)
        end
        file:close()
        os.sleep(5)
        os.execute("/tmp/flumph_script.lua")
    end):detach()
end
