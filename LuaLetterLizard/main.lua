require("config")
require("helper_functions")
require("games")
<<<<<<< HEAD

game_i = 0

function get_game()
    game_i += 1
    return games.easy[game_i]
end

game = get_game()
puzzle = game.letters

solutions = game.words
=======
games_letters = {}
games_letters = str_to_table(games.easy[1].letters)
games_words = {}
games_words = games.easy[1].words
--puzzle = {"R","A", "B", "L", "S", "T", "N", "E", "S"}
puzzle = table.shallow_copy(games_letters)
--solutions = {"STAB", "LAB", "BLARE", "TEN", "TAB"}
solutions = {}
solutions = table.shallow_copy(games_words)
>>>>>>> added some more functionality
letters_guessed = {}
puzzle_letters_displayed = table.shallow_copy(puzzle)
message = ""
score = 0
words_guessed_correct = {}
font = love.graphics.newFont(14)





function love.load()

    bg = {0,153,76}
    love.graphics.setBackgroundColor(bg)

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
            letters_guessed = {}
        end
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
        x = solved_words_region_left 
        y = solved_words_region_top + i*(square_width + spacing)
        love.graphics.print(letter, x + square_width/4, y + square_width/5)
    end
end

