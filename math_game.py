import random

def math_quiz_game():
    print("=" * 50)
    print("      Welcome to SmartStudywithAI - Math Quest!      ")
    print("=" * 50)
    print("USS / NuMaTS പരീക്ഷകൾക്കായുള്ള മാത്സ് ഗെയിമിലേക്ക് സ്വാഗതം!\n")
    
    score = 0
    level = 1
    total_questions = 3
    
    # Level 1: Basic Arithmetic Logic
    print(f"--- LEVEL {level}: നമ്പർ ലോജിക് ---")
    questions_l1 = [
        {"q": "2, 4, 8, 16, ... അടുത്ത സംഖ്യ ഏത്?", "a": "32"},
        {"q": "ഒരു സംഖ്യയുടെ 4 മടങ്ങിൽ നിന്ന് 5 കുറച്ചാൽ 15 കിട്ടും. സംഖ്യ ഏത്?", "a": "5"},
        {"q": "1 മുതൽ 10 വരെയുള്ള എണ്ണൽ സംഖ്യകളുടെ തുക എത്ര?", "a": "55"}
    ]
    
    for i, q in enumerate(questions_l1):
        print(f"ചോദ്യം {i+1}: {q['q']}")
        user_ans = input("ഉത്തരം നൽകുക: ").strip()
        if user_ans == q['a']:
            print("✅ ശരിയുത്തരം! +10 പോയിന്റ്സ്.\n")
            score += 10
        else:
            print(f"❌ തെറ്റാണ്. ശരിയുത്തരം: {q['a']}\n")
            
    # Level 2: Advanced Math Logic (NuMaTS style)
    if score >= 20:
        level = 2
        print(f"--- LEVEL {level}: അഡ്വാൻസ്ഡ് മാത്സ് ലോജിക് ---")
        print("അഭിനന്ദനങ്ങൾ! നിങ്ങൾ ലെവൽ 2-ലേക്ക് പ്രവേശിച്ചിരിക്കുന്നു.\n")
        
        questions_l2 = [
            {"q": "തുടർച്ചയായ മൂന്ന് എണ്ണൽ സംഖ്യകളുടെ തുക 30 ആയാൽ അതിലെ ഏറ്റവും വലിയ സംഖ്യ ഏത്?", "a": "11"},
            {"q": "ഒരു സമചതുരത്തിന്റെ വശം ഇരട്ടിയാക്കിയാൽ പരപ്പളവ് എത്ര മടങ്ങാകും?", "a": "4"}
        ]
        
        for i, q in enumerate(questions_l2):
            print(f"ചോദ്യം {i+1}: {q['q']}")
            user_ans = input("ഉത്തരം നൽകുക: ").strip()
            if user_ans == q['a']:
                print("✅ മികച്ചത്! ശരിയുത്തരം. +20 പോയിന്റ്സ്.\n")
                score += 20
            else:
                print(f"❌ തെറ്റാണ്. ശരിയുത്തരം: {q['a']}\n")
    else:
        print("ലെവൽ 2-ലേക്ക് പ്രവേശിക്കാൻ കുറഞ്ഞത് 20 പോയിന്റ് വേണം. വീണ്ടും ശ്രമിക്കൂ!")

    print("=" * 50)
    print(f"ഗെയിം പൂർത്തിയായി! നിങ്ങളുടെ ആകെ സ്കോർ: {score}")
    print("=" * 50)

if __name__ == "__main__":
    math_quiz_game()
