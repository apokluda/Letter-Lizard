function love.load()
  --preloading all game configurations and games

  require("Loveframes")
  games = require("games")
  --g = love.graphics
  --easygames = love.filesystem.load(games.lua)
  background = {0, 204, 102}
  tile_width = 50
  tile_height = 50
  tile_x = 100
  tile_y = 100
  holder_length = 50
  holder_x = 100
  holder_y = 300
  tiles = {}
  holder = {}
  love.graphics.setBackgroundColor(background)


  
end

function love.update(dt)
 --updating tile positions here?

  tile_x = tile_x*dt
  tile_y = tile_y*dt

 
  loveframes.update(dt)
end

function love.draw()
  --trying to generate tiles from the first easy game
   for i = 1, string.len(games.easy[1].letters) do
    tiles[i] = string.sub(games.easy[1].letters, i, i)
  end
  for k,v in pairs(tiles) do
    love.graphics.print("v",100,100,10)
    Button(v)
  end

  
  
 
  loveframes.draw()
end

function love.mousepressed(x,y,button)
  
  loveframes.mousepressed(x,y,button)
end

function love.mousereleased(x,y,button)
  
  loveframes.mousereleased(x,y,button)
end

function love.keypressed(key,unicode)

  loveframes.keypressed(key,unicode)

end

function love.keyreleased(key)
  
  loveframes.keyreleased(key)
end

function love.textinput(t)
   

    loveframes.textinput(text)
end


function Button(text)
  --creating tiles using buttons from loveframes library
  local button = loveframes.Create("button")
  button.Draw = function(self)
  button:SetSize(tile_width, tile_height):SetPos(tile_x , tile_y):SetText(text):Center()
  end

  button.OnMouseEnter = function(self)
    
  end

  button.OnClick = function(self, x, y)
    
  end
  button.OnMouseExit = function(self)
    
  end

end