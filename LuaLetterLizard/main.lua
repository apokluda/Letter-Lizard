require("config")
require("helper_functions")
require("games")
require("LoveFrames")
math.randomseed(os.time())
games_letters = {}
games_letters = str_to_table(games.easy[1].letters)
games_words = {}
games_words = games.easy[1].words
--puzzle = {"R","A", "B", "L", "S", "T", "N", "E", "S"}
puzzle = table.shallow_copy(games_letters)
--solutions = {"STAB", "LAB", "BLARE", "TEN", "TAB"}
solutions = {}
solutions = table.shallow_copy(games_words)
letters_guessed = {}
puzzle_letters_displayed = table.shallow_copy(puzzle)
message = ""
score = 0
words_guessed_correct = {}
font = love.graphics.newFont(14)
image = love.graphics.newImage( "good_job.png" )
clicked = false

function love.load()

    bg = {0,153,76}
    love.graphics.setBackgroundColor(bg)
    initTime = love.timer.getTime()
    correct = false

end

function love.keypressed(key)
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
            puzzle_letters_displayed = table.shallow_copy(puzzle)
            correct = true
            letters_guessed = {}
        end
    elseif (key == " ") then
        puzzle_letters_displayed = shuffled(puzzle_letters_displayed)
    end
end

function love.mousepressed(x, y, button)
    if (button == 'l') and (x > 100) and (x < 100 + button_width) and (y > 400) and (y < 400 + button_height)  then
        --clicked = true
        newgame()
    end
      
    loveframes.mousepressed(x, y, button)
end

function love.mousereleased(x , y, button)
    loveframes.mousereleased(x , y, button)
end
function love.update(dt)
    if (correct) then
        dt = dt * dt
    end

end

function love.draw()
    love.graphics.setColor(black)
    love.graphics.setFont(font)
    love.graphics.line(700,0, 700, 500)

    for i, letter in ipairs(letters_guessed) do
        x = letters_guessed_left + i * square_width + i * spacing
        y = letters_guessed_top
        love.graphics.rectangle("line", x, y ,square_width,square_width)
        love.graphics.print(letter, x + square_width/4, y + square_width/5)
    end
    for i, letter in ipairs(puzzle_letters_displayed) do
        x = puzzle_letters_left + i * square_width + i * spacing
        y = puzzle_letters_top
        love.graphics.rectangle("line", x, y ,square_width,square_width)
        love.graphics.print(letter, x + square_width/4, y + square_width/5)
    end
    for i, letter in ipairs(words_guessed_correct) do
        ht = love.graphics.getHeight()
        --x = solved_words_region_left 
        x = solved_words_col_margin
        --y = solved_words_region_top + i*(square_width + spacing)
        y = i *puzzle_letters_top
        love.graphics.print(letter, x + square_width/4, y + square_width/5)
    end

    if (correct) then
        love.graphics.setColor(255,255,255,255)
        love.graphics.draw( image, goodjob_x, goodjob_y)
        correct = false
    end

    love.graphics.rectangle("line",100, 400, button_width, button_height)
    --love.graphics.print("New Game", 100 + button_width/4, 400 + button_width/10)
    newgame_button = loveframes.Create("button")
    newgame_button:SetSize(button_width, button_height)
    newgame_button:SetPos(100, 400)
    newgame_button:SetText("New Game")
    if clicked then
        newgame_button:SetText("hi")
        --clicked = false
    end

    loveframes.draw()
end

function newgame()
    new_generator = math.random(1,100)
    games_letters = {}
    games_letters = str_to_table(games.easy[new_generator].letters)
    games_words = {}
    games_words = games.easy[new_generator].words
    --puzzle = {"R","A", "B", "L", "S", "T", "N", "E", "S"}
    puzzle = table.shallow_copy(games_letters)
    --solutions = {"STAB", "LAB", "BLARE", "TEN", "TAB"}
    solutions = {}
    solutions = table.shallow_copy(games_words)
    letters_guessed = {}
    puzzle_letters_displayed = table.shallow_copy(puzzle)

end
