#!/usr/bin/env lua5.2

games = dofile("games.lua")

menu = {"Start Game", "End Game"}

io.write("Letter Lizard\n")
io.write("Main Menu\n")
for k,v in pairs(menu) do
	print(k..":".." "..v)
end
io.write("Enter your option")




