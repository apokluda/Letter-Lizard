require("config")
require("helper_functions")
require("games")
require("LoveFrames")
Gamestate = require("gamestate")


local menu = {}
local game = {}
function menu:init()

    splash = love.graphics.newImage("splash.png")
end

function menu:draw()
    love.graphics.setColor(255,255,255,255)
    love.graphics.draw(splash, 0 ,0)
end

function menu:keypressed(key)
    if key == ' ' then
        Gamestate.switch(game)
    end
end

function love.load()
    Gamestate.registerEvents()
    Gamestate.switch(menu)
    
end

function game:init()
    math.randomseed(os.time())
    games_letters = {}
    games_letters = str_to_table(games.easy[1].letters)
    games_words = {}
    games_words = games.easy[1].words
    puzzle = table.shallow_copy(games_letters)
    solutions = {}
    solutions = table.shallow_copy(games_words)
    letters_guessed = {}
    puzzle_letters_displayed = table.shallow_copy(puzzle)
    message = ""
    score = 0
    words_guessed_correct = {}
    font = love.graphics.newFont(14)
    goodjob = love.graphics.newImage( "good_job.png" )
    game_over_image = love.graphics.newImage("game_over.png")
    time_up = love.graphics.newImage("time_up.png")
    number_fnt_40 = love.graphics.newFont( "funfont.ttf", 40)
    number_fnt_20 = love.graphics.newFont("funfont.ttf", 20)
    score = 0
    quit_game = false
    remaining_time = 120
    gameover = false
    correct = false
    timer = 0
    target = 5
    bg = {0,153,76}
    love.graphics.setBackgroundColor(bg)

end

function game:keypressed(key)
    if (isalpha_char(key)) then key = key:upper() end

    if (array_contains(puzzle_letters_displayed, key)) then
        table.insert(letters_guessed, key)
        remove_item(puzzle_letters_displayed, key)
    elseif (key == "backspace") then
        if (#letters_guessed >= 1) then
            letter_to_delete = letters_guessed[#letters_guessed]
            table.remove(letters_guessed, #letters_guessed)
            table.insert(puzzle_letters_displayed, letter_to_delete)
        end
    elseif (key == "return") then
        guess = build_str_from_arr(letters_guessed)
        if (array_contains(solutions, guess) and (not array_contains(words_guessed_correct, guess))) then
            table.insert(words_guessed_correct, guess)
            score = score + (#guess)
            puzzle_letters_displayed = table.shallow_copy(puzzle)
            correct = true
            letters_guessed = {}
        end
    elseif (key == " ") then
        puzzle_letters_displayed = shuffled(puzzle_letters_displayed)
    end
end

function game:mousepressed(x, y, button)
    if (button == 'l') and (x > 100) and (x < 100 + button_width) and (y > 400) and (y < 400 + button_height)  then
        game:newgame()
        --gameover = false
    elseif (button == 'l') and (x > 300) and (x < 300 + button_width) and (y > 400) and (y < 400 + button_height)  then
        puzzle_letters_displayed = shuffled(puzzle_letters_displayed)
    elseif (button == 'l') and (x > 500) and (x < 500 + button_width) and (y > 400) and (y < 400 + button_height)  then
        love.event.quit()
    end

      
    loveframes.mousepressed(x, y, button)
end

function game:update(dt)
    -- updating display time for 'good_job!'
    timer = timer + dt
    --updating game time
    remaining_time = remaining_time - dt 
    if remaining_time <= 0 then
        gameover = true
        remaining_time = 0
    end
end

function game:draw()
    love.graphics.setColor(black)
    love.graphics.line(700,0, 700, 500)

    for i, letter in ipairs(letters_guessed) do
        x = letters_guessed_left + i * square_width + i * spacing
        y = letters_guessed_top
        love.graphics.rectangle("line", x, y ,square_width,square_width)
        love.graphics.setFont(number_fnt_40)
        love.graphics.print(letter, x + square_width/4, y + square_width/5)
    end
    for i, letter in ipairs(puzzle_letters_displayed) do
        x = puzzle_letters_left + i * square_width + i * spacing
        y = puzzle_letters_top
        love.graphics.rectangle("line", x, y ,square_width,square_width)
        love.graphics.setFont(number_fnt_40)
        love.graphics.print(letter, x + square_width/4, y + square_width/5)
    end
    for i, letter in ipairs(words_guessed_correct) do
        x = solved_words_col_margin
        y = i * 60
        love.graphics.setFont(number_fnt_20)
        love.graphics.print(letter, x + square_width/4, y + square_width/5)

    end

    --display time up!
    if gameover then
        love.graphics.setColor(255,255,255,255)
        love.graphics.draw(time_up, goodjob_x, goodjob_y)
    end

    --display countdown timer
    local minutes = math.floor( remaining_time / 60 ) -- calculate how many minutes are left
    local seconds = math.floor( remaining_time % 60 ) -- calculate how many seconds are left
    love.graphics.setFont(number_fnt_40)
    love.graphics.print( string.format("%02d:%02d",minutes,seconds), 900, 20 )
    love.graphics.rectangle("line",100, 400, button_width, button_height)
    love.graphics.rectangle("line",300, 400, button_width, button_height)
    love.graphics.rectangle("line",500, 400, button_width, button_height)

    --displaying the score
    love.graphics.setFont(number_fnt_40)
    love.graphics.print("Score:", 710, 20)
    love.graphics.print(score, 840, 20 )
    newgame_button = loveframes.Create("button")
    newgame_button:SetSize(button_width, button_height)
    newgame_button:SetPos(100, 400)
    newgame_button:SetText("NEW GAME")
    shuffle_button = loveframes.Create("button")
    shuffle_button:SetSize(button_width, button_height)
    shuffle_button:SetPos(300, 400)
    shuffle_button:SetText("SHUFFLE")
    quit_button = loveframes.Create("button")
    quit_button:SetSize(button_width, button_height)
    quit_button:SetPos(500, 400)
    quit_button:SetText("QUIT")


    --display Good Job!
    if correct and timer <= 2 then
        love.graphics.setColor(255,255,255,255)
        love.graphics.draw( goodjob, goodjob_x, goodjob_y)
    else
        timer = 0
        correct = false
    end

    loveframes.draw()
end

function game:newgame()
    new_generator = math.random(1,100)
    games_letters = {}
    games_letters = str_to_table(games.easy[new_generator].letters)
    games_words = {}
    games_words = games.easy[new_generator].words
    puzzle = table.shallow_copy(games_letters)
    solutions = {}
    solutions = table.shallow_copy(games_words)
    letters_guessed = {}
    puzzle_letters_displayed = table.shallow_copy(puzzle)
    words_guessed_correct = {}
    gameover = false
    remaining_time = 120
    score = 0
end

function game:quit()

    love.graphics.setFont(number_fnt_40)
    love.graphics.print("Thank You For Playing the Game!", goodjob_x, goodjob_y)

end