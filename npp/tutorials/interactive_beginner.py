"""
Interactive Beginner Tutorial Engine for N++
Runs step-by-step lessons with live N++ code execution and interactive prompts.
"""

import sys
import os
import time

# Ensure npp package is importable
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from npp import run_code


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def pause(prompt="Press ENTER to continue to the next lesson..."):
    print("\n" + "-" * 70)
    input(f"  👉 {prompt}")
    print("-" * 70)


def header(title, step_num, total=8):
    clear()
    print("=" * 75)
    print(f"   🌟 N++ INTERACTIVE BEGINNER TUTORIAL — LESSON {step_num} OF {total}")
    print(f"      {title.upper()}")
    print("=" * 75)
    print()


def run_demo(code_str):
    print("  [Code in N++]")
    for line in code_str.strip().splitlines():
        print(f"    | {line}")
    print("\n  [Live Execution Output]")
    print("  " + "-" * 40)
    run_code(code_str)
    print("  " + "-" * 40)


def lesson_1():
    header("Talking to the Screen: 'say'", 1)
    print("""
  In real life, when you want to speak, you talk.
  In N++, you tell the computer to speak using the English word 'say'!
  Anything inside quotes ("...") is text.
    """)
    code = """
say "Hello! Welcome to N++."
say "Coding here is literally as easy as writing English sentences!"
    """
    run_demo(code)
    pause()


def lesson_2():
    header("Remembering Things: 'set ... to ...'", 2)
    print("""
  Analogy: A labeled storage box.
  When you want the computer to remember a number or word, you say:
      set <name> to <value>
  
  And when you want to change what's inside the box later:
      change <name> to <new_value>
    """)
    code = """
set player_name to "Hero"
set score to 100
say "Player: " + player_name + ", Current Score: " + score

change score to 150
say "Bonus points collected! New Score: " + score
    """
    run_demo(code)
    pause()


def lesson_3():
    header("Asking Questions: 'ask'", 3)
    print("""
  Analogy: The computer asking you a question and listening for your reply.
  In N++, you write:
      set answer to ask "What is your name? "
    """)
    print("  Let's run this live with YOUR input right now!\n")
    code = """
set user_name to ask "What is your name? "
say "Awesome to meet you, " + user_name + "! Welcome to N++."
    """
    run_demo(code)
    pause()


def lesson_4():
    header("Making Decisions: 'if' and 'otherwise'", 4)
    print("""
  Analogy: A fork in the road:
  "If it is hot outside, wear shorts; otherwise, wear a jacket."
  
  In N++, you write comparisons using natural English words:
    * is greater than
    * is less than
    * is at least
    * is not
    * is (equals)
    """)
    code = """
set temperature to 28

if temperature is greater than 30 then
    say "It is very hot outside! Stay hydrated."
otherwise if temperature is less than 15 then
    say "It is chilly outside! Grab a warm coat."
otherwise
    say "The weather is lovely and pleasant outside!"
end
    """
    run_demo(code)
    pause()


def lesson_5():
    header("Repeating Actions: 'repeat N times'", 5)
    print("""
  Analogy: Doing 3 jumping jacks in gym class.
  Instead of copying and pasting the same line multiple times,
  just write: repeat 3 times ... end!
    """)
    code = """
say "Let's cheer 3 times:"
repeat 3 times
    say "  🎉 Hip Hip Hooray!"
end
    """
    run_demo(code)
    pause()


def lesson_6():
    header("Shopping Lists: 'for each'", 6)
    print("""
  Analogy: Checking items on a grocery shopping list one by one.
  Put items inside brackets [ ... ] and look through them using:
      for each item in list ... end
    """)
    code = """
set favorites to ["Pizza", "Tacos", "Ice Cream", "Mango"]

say "Here are delicious foods:"
for each food in favorites
    say "  * I love eating: " + food
end
    """
    run_demo(code)
    pause()


def lesson_7():
    header("Teaching the Computer a Recipe (Functions)", 7)
    print("""
  Analogy: Writing down a recipe card once, so anyone can cook it anytime!
  In N++, you teach new actions using:
      to <action_name> with <inputs>
          give back <result>
      end
    """)
    code = """
to calculate_total with price, tax_rate
    give back price + (price * tax_rate)
end

set total to calculate_total(100, 0.15)
say "Original Price: $100. Total with 15% tax: $" + total
    """
    run_demo(code)
    pause()


def lesson_8():
    header("Your Turn! Mini Interactive Playground", 8)
    print("""
  Congratulations! You have completed all beginner lessons!
  Now it's your turn to try writing a line of N++ code.
  
  Example ideas to type:
    say "I am now an N++ coder!"
    25 * 4
    repeat 2 times say "Testing!" end
    """)
    while True:
        try:
            user_input = input("  Enter N++ code (or press ENTER to finish): ").strip()
            if not user_input:
                break
            print("  Result:")
            run_code(user_input)
            print()
        except (KeyboardInterrupt, EOFError):
            break

    clear()
    print("=" * 75)
    print("   🏆 CONGRATULATIONS! YOU HAVE GRADUATED FROM THE BEGINNER GUIDE!")
    print("=" * 75)
    print("""
  You now understand:
    ✓ say (Talking)
    ✓ set ... to ... (Variables)
    ✓ ask (Input)
    ✓ if / otherwise (Decisions)
    ✓ repeat (Loops)
    ✓ for each (Lists)
    ✓ to ... with ... (Functions)

  Next Recommended Step:
    Run 'tutorial_web.bat' to learn how to build websites 1000x faster than HTML!
    """)
    input("  Press ENTER to return to the launcher...")


def main():
    lesson_1()
    lesson_2()
    lesson_3()
    lesson_4()
    lesson_5()
    lesson_6()
    lesson_7()
    lesson_8()


if __name__ == "__main__":
    main()
