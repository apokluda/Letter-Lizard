#!/usr/bin/env lua5.2

games = dofile("games.lua")

io.write("The letters for the first easy game are " .. games.easy[1].letters .. ".\n")
io.write("These letters can form " .. #games.easy[1].words .. " words.\n")
io.write("The first word is " .. games.easy[1].words[1] .. ". Can you find the rest?\n")

