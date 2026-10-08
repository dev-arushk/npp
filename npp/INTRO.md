# Welcome to N++ (Beginner's Introduction)

> **Programming in N++ is as simple as writing plain English sentences!**

---

## 🚀 30-Second Quickstart

To run an N++ script:
```powershell
.\npp.bat examples\intro_basics.npp
```
*(or `python main.py examples\intro_basics.npp`)*

To start the interactive sandbox (REPL):
```powershell
.\npp.bat repl
```

---

## 📖 The Plain English Cheat Sheet

| What you want to do | How to write it in N++ | What it does |
|:---|:---|:---|
| **Say something** | `say "Hello world!"` | Prints text to the screen |
| **Ask the user** | `set name to ask "Your name? "` | Asks user for text input |
| **Save a number** | `set age to 21` | Creates variable `age` |
| **Change a variable** | `change age to 22` | Updates the variable |
| **Compare values** | `if age is greater than 18 then ... end` | Checks a condition |
| **Otherwise branch** | `if x is 5 then ... otherwise ... end` | Else branch |
| **Repeat an action** | `repeat 3 times ... end` | Runs the body 3 times |
| **Go through items** | `for each item in ["a", "b"] ... end` | Iterates over each item |
| **Create a function**| `to add with a, b give back a + b end` | Defines reusable action |
| **Leave a note** | `// my note` or `# note` | Adds a comment |

---

## 🌟 Step-by-Step Tutorial

### 1. Talking to the Screen
To make your computer say something, write:
```npp
say "Good morning!"
say "Welcome to N++"
```

### 2. Variables (Remembering Things)
To save a piece of information:
```npp
set hero to "Arthur"
set level to 10
say "Hero: " + hero + ", Level: " + level
```
Notice that combining text and numbers with `+` just works automatically!

To change a variable later:
```npp
change level to 11
say "Level up! Now at level: " + level
```

### 3. Asking Questions
You can prompt the user for input using `ask`:
```npp
set favorite_food to ask "What is your favorite food? "
say "Yum! I like " + favorite_food + " too!"
```

### 4. Making Decisions (`if` / `otherwise`)
Write conditions like you speak:
```npp
set score to 88

if score is greater than 90 then
    say "Grade: Outstanding!"
otherwise if score is greater than 75 then
    say "Grade: Good job!"
otherwise
    say "Grade: Keep trying!"
end
```

English comparison words supported:
- `is` or `equals` (equal to)
- `is not` (not equal)
- `is greater than` (greater than)
- `is less than` (less than)
- `is at least` (greater than or equal to)
- `is at most` (less than or equal to)
- `and`, `or`, `not`

### 5. Repeating Actions (`repeat`)
When you want to do something several times:
```npp
repeat 5 times
    say "Hello!"
end
```

### 6. Working with Lists (`for each`)
Create a list with square brackets `[...]` and go through it:
```npp
set animals to ["cat", "dog", "fox"]

for each pet in animals
    say "I have a " + pet
end
```

### 7. Reusable Actions (Functions)
You can teach N++ new actions using `to ... with ...`:
```npp
to greet with person_name
    give back "Hello, " + person_name + "!"
end

set message to greet("Taylor")
say message
```

---

## 🛠️ Built-in Helper Functions

N++ comes with helpful built-in tools:

- `len(item)`: Length of a list, text, or map.
- `range(10)`: Generates numbers from `0` to `9`.
- `range(1, 11)`: Generates numbers from `1` to `10`.
- `push(list, item)`: Adds an item to a list.
- `pop(list)`: Removes the last item from a list.
- `upper(text)`: Converts text to UPPERCASE.
- `lower(text)`: Converts text to lowercase.
- `abs(number)`: Absolute value.
- `round(number)`: Rounds a number.
- `time()`: Current timestamp.
- `sleep(seconds)`: Pauses execution.

---

## 🎯 Next Steps
Check out the ready-to-run examples in the `examples/` folder:
- [intro_basics.npp](file:///C:/Users/kulka/.gemini/antigravity/scratch/npp/examples/intro_basics.npp)
- [simple_english.npp](file:///C:/Users/kulka/.gemini/antigravity/scratch/npp/examples/simple_english.npp)
- [fizzbuzz.npp](file:///C:/Users/kulka/.gemini/antigravity/scratch/npp/examples/fizzbuzz.npp)
- [fibonacci.npp](file:///C:/Users/kulka/.gemini/antigravity/scratch/npp/examples/fibonacci.npp)
