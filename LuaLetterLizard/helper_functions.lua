function isalpha_char(s)
    if (s:len() > 1) then return false end
    if (s:match("%a")) then
        return true
    else
        return false
    end

end

function print_array(arr)
    for i = 1, (#arr) do
        print(arr[i])
    end
end

function array_contains(arr, item)
    for i, x in ipairs(arr) do
        if (x == item) then
            return true
        end
    end
    return false
end

function addToSet(set, key)
    set[key] = true
end

function removeFromSet(set, key)
    set[key] = nil
end

function setContains(set, key)
    return set[key] ~= nil
end

function indexof(t,val)
    for k,v in ipairs(t) do 
        if v == val then return k end
    end
end

function remove_item(arr, val)
    index = indexof(arr, val)
    table.remove(arr, index)
end

function table.shallow_copy(t)
  local t2 = {}
  for k,v in pairs(t) do
    t2[k] = v
  end
  return t2
end

function build_str_from_arr(arr)
    s = ""
    for i, c in ipairs(arr) do
        s = s..c
    end
    return s
end