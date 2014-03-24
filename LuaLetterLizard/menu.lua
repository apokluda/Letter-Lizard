--Gamestate = require("gamestate")
require ("config")

local menu = {} -- previously: Gamestate.new()
--local game = {}

function menu:init()
	splash = love.graphics.newImage(splash.png)
end

function menu:draw()
    love.graphics.draw(splash, game_width, game_height)
end

