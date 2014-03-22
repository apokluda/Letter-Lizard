--require("main")
require("helper_functions")
--print(isalpha("5"))

x = {"a","b", "c","d"}
--addToSet(x, "a")
--addToSet(x, "b")
--print("hello")
--print_set(x)
--x[1] = 5
--x[2] = 6
--print(array_contains(x, 5))
remove_item(x,"b")
print_array(x)
print(array_contains(x, "c"))

puzzle = {"R","A", "B", "L", "S", "T", "N", "E", "S"}
solutions = {"STAB", "LAB", "BLARE", "TEN", "TAB"}
letters_guessed = {}
puzzle_letters_displayed = table.shallow_copy(puzzle)
--print_array(puzzle_letters_displayed)
key = "R"
print(array_contains(puzzle_letters_displayed, key))
-- if (isalpha(key) and array_contains(puzzle_letters_displayed, key)) then
--         table.insert(letters_guessed, key)
--         remove_item(puzzle_letters_displayed, key)
--         --shoot()
-- end

print(build_str_from_arr({"a", "b", "c"}))
