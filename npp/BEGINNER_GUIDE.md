# The Complete Beginner's Guide to N++ 🌟

> **Never coded before? Don't worry! This guide is written specially for you.**  
> Coding in **N++** is just like giving instructions to a friend in simple English.

---

## 🎯 How to Test N++ Right Now (Choose 1 Way)

You do **not** need to be a computer wizard to test N++. Here are the 3 simplest ways:

### 🏆 Method 1: The Easiest Way (Just Double-Click!)
1. Open your Windows File Explorer.
2. Go to this folder:
   ```
   C:\Users\kulka\.gemini\antigravity\scratch\npp
   ```
3. Double-click on the file named **`play.bat`**.
4. A black-and-white window will open showing a menu:
   ```
   [1] Take the Step-by-Step Guided Tour (guided_tour.npp)
   [2] Run the Beginner Basics Script (intro_basics.npp)
   [3] Run the Plain English Weather Script (simple_english.npp)
   [4] Start Interactive Mode (type code live!)
   [5] Run Automated Health Check (all 12 tests)
   [6] Exit
   ```
5. Type **`1`** on your keyboard and press **Enter**!
6. It will guide you step by step!

---

### 💻 Method 2: Running from the Terminal / PowerShell
If you have a terminal or command prompt open:
1. Open PowerShell.
2. Type these commands one by one and press **Enter**:
   ```powershell
   cd C:\Users\kulka\.gemini\antigravity\scratch\npp
   .\npp.bat examples\intro_basics.npp
   ```
3. You will immediately see N++ run and print out the results on your screen!

---

### 💬 Method 3: Talk to N++ Live (Interactive Sandbox)
Want to test commands one line at a time?
1. In PowerShell, type:
   ```powershell
   cd C:\Users\kulka\.gemini\antigravity\scratch\npp
   .\npp.bat repl
   ```
2. You will see:
   ```
   n++>
   ```
3. Type:
   ```npp
   say "Hello!"
   ```
   and press **Enter**. N++ will immediately print:
   ```
   Hello!
   ```
4. Type:
   ```npp
   2 + 3
   ```
   and press **Enter**. N++ will tell you:
   ```
   => 5
   ```
5. When you are done, type `exit` to leave.

---

## 🧠 Coding Concepts Explained with Everyday Analogies

### 1. Talking to the Screen (`say`)
* **Real-life analogy**: The computer speaking out loud.
* **How you write it**:
  ```npp
  say "Good morning, world!"
  ```
* Anything inside quotes (`"..."`) is text (called a **String**).

---

### 2. Remembering Things (`set ... to ...`)
* **Real-life analogy**: Writing a note on a sticky label and sticking it on a box.
* **How you write it**:
  ```npp
  set my_points to 100
  set player_name to "Hero"
  ```
* The box is named `my_points`, and inside it is the number `100`.
* You can change what's in the box anytime:
  ```npp
  change my_points to 150
  ```

---

### 3. Asking Questions (`ask`)
* **Real-life analogy**: The computer asking you a question and waiting for your answer.
* **How you write it**:
  ```npp
  set name to ask "What is your name? "
  say "Hello, " + name + "!"
  ```

---

### 4. Making Decisions (`if` / `otherwise`)
* **Real-life analogy**: A fork in the road: *"If it rains, bring an umbrella; otherwise, wear sunglasses."*
* **How you write it**:
  ```npp
  set temperature to 32

  if temperature is greater than 30 then
      say "It is hot outside!"
  otherwise
      say "It is cool outside!"
  end
  ```
* Notice that every decision block finishes with the word **`end`**.

#### English Comparison Words:
| What you say | What it means | Example |
|---|---|---|
| `is` | Equal to | `if score is 100 then ... end` |
| `is not` | Not equal to | `if name is not "Bob" then ... end` |
| `is greater than` | Bigger than | `if score is greater than 50 then ... end` |
| `is less than` | Smaller than | `if age is less than 18 then ... end` |
| `is at least` | Greater than or equal | `if level is at least 5 then ... end` |
| `is at most` | Less than or equal | `if price is at most 20 then ... end` |

---

### 5. Doing Something Multiple Times (`repeat`)
* **Real-life analogy**: Jumping 3 times in gym class.
* **How you write it**:
  ```npp
  repeat 3 times
      say "Jumping!"
  end
  ```
* Output:
  ```
  Jumping!
  Jumping!
  Jumping!
  ```

---

### 6. Lists of Items (`for each`)
* **Real-life analogy**: A shopping grocery list.
* **How you write it**:
  ```npp
  set groceries to ["Milk", "Eggs", "Bread", "Apples"]

  for each item in groceries
      say "Remember to buy: " + item
  end
  ```

---

### 7. Creating Your Own Recipe/Action (`to ... with ...`)
* **Real-life analogy**: Teaching someone a recipe once, then asking them to make it whenever you want.
* **How you write it**:
  ```npp
  to double_number with x
      give back x * 2
  end
  ```
* Now you can use it anytime:
  ```npp
  say double_number(5)   // Prints 10
  say double_number(50)  // Prints 100
  ```

---

## 📝 How to Create Your Very Own N++ Program

You can make your own program in 3 steps:

1. Open **Notepad** on your computer.
2. Type your code, for example:
   ```npp
   say "=== MY FIRST PROGRAM ==="
   set name to ask "Who are you? "
   say "Welcome to coding, " + name + "!"
   repeat 3 times
       say "You are awesome!"
   end
   ```
3. Save the file inside `C:\Users\kulka\.gemini\antigravity\scratch\npp\my_program.npp`.
4. Run it in terminal:
   ```powershell
   .\npp.bat my_program.npp
   ```
   Or open `play.bat`!
