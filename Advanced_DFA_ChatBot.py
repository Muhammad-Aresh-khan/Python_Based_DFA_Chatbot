import json
import random
import time
import os
from datetime import datetime
from collections import defaultdict
import re
from difflib import SequenceMatcher

class AdvancedDFAChatbot:
    def __init__(self):
        self.dfas = {
            "hi": {
                "dfa": {
                    "q0": {'h': 'q1'},
                    "q1": {'i': 'q2'},
                    "q2": {}
                },
                "accept": "q2",
                "responses": [
                    "Hello! 👋 Great to see you!",
                    "Hi there! How can I help you today?",
                    "Hey! Welcome to our DFA-powered chat!"
                ],
                "category": "greeting",
                "priority": 1
            },
            "hello": {
                "dfa": {
                    "q0": {'h': 'q1'},
                    "q1": {'e': 'q2'},
                    "q2": {'l': 'q3'},
                    "q3": {'l': 'q4'},
                    "q4": {'o': 'q5'},
                    "q5": {}
                },
                "accept": "q5",
                "responses": [
                    "Hello! 🌟 Nice to meet you!",
                    "Greetings! How are you doing today?",
                    "Hello there! Ready to chat?"
                ],
                "category": "greeting",
                "priority": 1
            },
            "how are you": {
                "dfa": {
                    "q0": {'h': 'q1'},
                    "q1": {'o': 'q2'},
                    "q2": {'w': 'q3'},
                    "q3": {' ': 'q4'},
                    "q4": {'a': 'q5'},
                    "q5": {'r': 'q6'},
                    "q6": {'e': 'q7'},
                    "q7": {' ': 'q8'},
                    "q8": {'y': 'q9'},
                    "q9": {'o': 'q10'},
                    "q10": {'u': 'q11'},
                    "q11": {}
                },
                "accept": "q11",
                "responses": [
                    "I'm functioning perfectly! 🚀 Thanks for asking!",
                    "Doing great! My DFA states are all working smoothly! ⚡",
                    "Excellent! Ready to process your inputs efficiently! 💫",
                    "I'm doing well! How about you?"
                ],
                "category": "status",
                "priority": 2
            },
            "what is your name": {
                "dfa": {
                    "q0": {'w': 'q1'},
                    "q1": {'h': 'q2'},
                    "q2": {'a': 'q3'},
                    "q3": {'t': 'q4'},
                    "q4": {' ': 'q5'},
                    "q5": {'i': 'q6'},
                    "q6": {'s': 'q7'},
                    "q7": {' ': 'q8'},
                    "q8": {'y': 'q9'},
                    "q9": {'o': 'q10'},
                    "q10": {'u': 'q11'},
                    "q11": {'r': 'q12'},
                    "q12": {' ': 'q13'},
                    "q13": {'n': 'q14'},
                    "q14": {'a': 'q15'},
                    "q15": {'m': 'q16'},
                    "q16": {'e': 'q17'},
                    "q17": {}
                },
                "accept": "q17",
                "responses": [
                    "I'm DFA-Bot! 🤖 A chatbot powered by Deterministic Finite Automata!",
                    "You can call me AutomataBot! I speak the language of state machines! ⚙️",
                    "I'm your friendly DFA assistant!"
                ],
                "category": "identity",
                "priority": 2
            },
            "good bye": {
                "dfa": {
                    "q0": {'g': 'q1'},
                    "q1": {'o': 'q2'},
                    "q2": {'o': 'q3'},
                    "q3": {'d': 'q4'},
                    "q4": {' ': 'q5'},
                    "q5": {'b': 'q6'},
                    "q6": {'y': 'q7'},
                    "q7": {'e': 'q8'},
                    "q8": {}
                },
                "accept": "q8",
                "responses": [
                    "Goodbye! 👋 Have an amazing day ahead!",
                    "See you later! Thanks for chatting with me! 🌟",
                    "Farewell! Hope to see you again soon! ✨"
                ],
                "category": "farewell",
                "priority": 1
            },
            "tell me a joke": {
                "dfa": {
                    "q0": {'t': 'q1'},
                    "q1": {'e': 'q2'},
                    "q2": {'l': 'q3'},
                    "q3": {'l': 'q4'},
                    "q4": {' ': 'q5'},
                    "q5": {'m': 'q6'},
                    "q6": {'e': 'q7'},
                    "q7": {' ': 'q8'},
                    "q8": {'a': 'q9'},
                    "q9": {' ': 'q10'},
                    "q10": {'j': 'q11'},
                    "q11": {'o': 'q12'},
                    "q12": {'k': 'q13'},
                    "q13": {'e': 'q14'},
                    "q14": {}
                },
                "accept": "q14",
                "responses": [
                    "Why do programmers prefer dark mode? Because light attracts bugs! 🐛💡",
                    "What do you call a DFA that tells jokes? A Finite State Machine with infinite humor! 😄",
                    "Why did the automaton go to therapy? It had too many state transitions! 🤖💭",
                    "How do you comfort a JavaScript bug? You console it! 😂"
                ],
                "category": "entertainment",
                "priority": 3
            },
            "what can you do": {
                "dfa": {
                    "q0": {'w': 'q1'},
                    "q1": {'h': 'q2'},
                    "q2": {'a': 'q3'},
                    "q3": {'t': 'q4'},
                    "q4": {' ': 'q5'},
                    "q5": {'c': 'q6'},
                    "q6": {'a': 'q7'},
                    "q7": {'n': 'q8'},
                    "q8": {' ': 'q9'},
                    "q9": {'y': 'q10'},
                    "q10": {'o': 'q11'},
                    "q11": {'u': 'q12'},
                    "q12": {' ': 'q13'},
                    "q13": {'d': 'q14'},
                    "q14": {'o': 'q15'},
                    "q15": {}
                },
                "accept": "q15",
                "responses": [
                    "I can understand patterns using DFA! 🎯 I respond to greetings, questions, and more!",
                    "I process text through finite state machines! Try different phrases and watch my DFA traces! ⚡",
                    "I can chat, tell jokes, answer questions, and learn new patterns!"
                ],
                "category": "capability",
                "priority": 2
            },
            "good morning": {
                "dfa": {
                    "q0": {'g': 'q1'},
                    "q1": {'o': 'q2'},
                    "q2": {'o': 'q3'},
                    "q3": {'d': 'q4'},
                    "q4": {' ': 'q5'},
                    "q5": {'m': 'q6'},
                    "q6": {'o': 'q7'},
                    "q7": {'r': 'q8'},
                    "q8": {'n': 'q9'},
                    "q9": {'i': 'q10'},
                    "q10": {'n': 'q11'},
                    "q11": {'g': 'q12'},
                    "q12": {}
                },
                "accept": "q12",
                "responses": [
                    "Good morning to you too! ☀️",
                    "Morning! Hope you have a wonderful day! 🌅",
                    "Good morning! Ready to start the day with some DFA magic? ✨"
                ],
                "category": "greeting",
                "priority": 1
            },
            "thank you": {
                "dfa": {
                    "q0": {'t': 'q1'},
                    "q1": {'h': 'q2'},
                    "q2": {'a': 'q3'},
                    "q3": {'n': 'q4'},
                    "q4": {'k': 'q5'},
                    "q5": {' ': 'q6'},
                    "q6": {'y': 'q7'},
                    "q7": {'o': 'q8'},
                    "q8": {'u': 'q9'},
                    "q9": {}
                },
                "accept": "q9",
                "responses": [
                    "You're welcome! 😊",
                    "My pleasure! Happy to help! 🤗",
                    "Anytime! That's what I'm here for! 💫"
                ],
                "category": "politeness",
                "priority": 2
            }
        }
        
        self.stats = {
            'total_messages': 0,
            'matched_messages': 0,
            'pattern_usage': defaultdict(int),
            'session_start': datetime.now(),
            'conversation_history': [],
            'user_patterns': set()
        }
        
        self.settings = {
            'show_traces': True,
            'fuzzy_matching': True,
            'learning_mode': True,
            'auto_save': True,
            'response_delay': 0.5
        }
        
        self.load_custom_patterns()
        self.print_welcome()
    
    def print_welcome(self):
        print("=" * 60)
        print("🤖 ADVANCED DFA CHATBOT SYSTEM")
        print("=" * 60)
        print("🚀 Features:")
        print("   • DFA Pattern Matching with Traces")
        print("   • Fuzzy String Matching")
        print("   • Dynamic Pattern Learning")
        print("   • Conversation Analytics")
        print("   • Export/Import Capabilities")
        print("   • Multiple Response Variations")
        print("-" * 60)
        print("📋 Commands:")
        print("   • 'help' - Show all commands")
        print("   • 'stats' - Show conversation statistics")
        print("   • 'patterns' - List all patterns")
        print("   • 'learn' - Enter learning mode")
        print("   • 'export' - Export conversation")
        print("   • 'settings' - Modify settings")
        print("   • 'clear' - Clear conversation history")
        print("   • 'exit/quit/bye' - End conversation")
        print("=" * 60)
        print()
    
    def run_dfa_with_trace(self, dfa_dict, accept_state, input_str):
        """Enhanced DFA runner with detailed trace"""
        state = "q0"
        trace = [f"Start: {state}"]
        accepted_chars = []
        
        for i, ch in enumerate(input_str):
            if ch in dfa_dict[state]:
                next_state = dfa_dict[state][ch]
                trace.append(f"'{ch}' → {next_state}")
                accepted_chars.append(ch)
                state = next_state
            else:
                trace.append(f"'{ch}' → REJECT (no transition from {state})")
                return {
                    'accepted': False, 
                    'trace': trace, 
                    'final_state': state,
                    'processed_chars': accepted_chars,
                    'remaining_input': input_str[i:]
                }
        
        accepted = state == accept_state
        trace.append(f"Final: {state} ({'ACCEPT' if accepted else 'REJECT'})")
        
        return {
            'accepted': accepted, 
            'trace': trace, 
            'final_state': state,
            'processed_chars': accepted_chars,
            'remaining_input': ''
        }
    
    def fuzzy_match(self, input_str, pattern, threshold=0.75):
        """Fuzzy string matching using sequence matcher"""
        if not self.settings['fuzzy_matching']:
            return False
        
        similarity = SequenceMatcher(None, input_str.lower(), pattern.lower()).ratio()
        return similarity >= threshold
    
    def find_best_match(self, user_input):
        """Find the best matching pattern using various techniques"""
        user_input = user_input.lower().strip()
        
        # First try exact DFA matching
        for pattern, data in self.dfas.items():
            result = self.run_dfa_with_trace(data["dfa"], data["accept"], user_input)
            if result['accepted']:
                return {
                    'type': 'exact',
                    'pattern': pattern,
                    'data': data,
                    'result': result,
                    'confidence': 1.0
                }
        
        # Then try fuzzy matching
        if self.settings['fuzzy_matching']:
            best_fuzzy = None
            best_similarity = 0
            
            for pattern, data in self.dfas.items():
                similarity = SequenceMatcher(None, user_input, pattern).ratio()
                if similarity > best_similarity and similarity >= 0.75:
                    best_similarity = similarity
                    best_fuzzy = {
                        'type': 'fuzzy',
                        'pattern': pattern,
                        'data': data,
                        'result': {'trace': [f"Fuzzy match: '{pattern}' (similarity: {similarity:.2%})"]},
                        'confidence': similarity
                    }
            
            if best_fuzzy:
                return best_fuzzy
        
        # Check for partial matches or suggestions
        suggestions = self.get_suggestions(user_input)
        return {
            'type': 'no_match',
            'suggestions': suggestions,
            'confidence': 0.0
        }
    
    def get_suggestions(self, user_input):
        """Get pattern suggestions based on partial matches"""
        suggestions = []
        user_input = user_input.lower()
        
        for pattern in self.dfas.keys():
            if pattern.startswith(user_input[:3]) or user_input[:3] in pattern:
                suggestions.append(pattern)
        
        return suggestions[:3]
    
    def generate_response(self, match_result, user_input):
        """Generate contextual response based on match result"""
        if match_result['type'] == 'exact':
            responses = match_result['data']['responses']
            response = random.choice(responses)
            
            # Update usage statistics
            self.stats['pattern_usage'][match_result['pattern']] += 1
            self.stats['matched_messages'] += 1
            
            return response, match_result['result']['trace']
            
        elif match_result['type'] == 'fuzzy':
            responses = match_result['data']['responses']
            response = f"I think you meant: {random.choice(responses)}"
            self.stats['matched_messages'] += 1
            
            return response, match_result['result']['trace']
            
        else:
            # No match found
            fallback_responses = [
                "I don't understand that yet! 🤔",
                "Hmm, my DFA couldn't match that pattern. 💭",
                "That's not in my vocabulary yet! 🎯",
                "I'm still learning that phrase! 📚"
            ]
            
            response = random.choice(fallback_responses)
            
            if match_result.get('suggestions'):
                response += f"\n💡 Maybe try: {', '.join(match_result['suggestions'])}"
            
            return response, ["No matching DFA pattern found"]
    
    def learn_new_pattern(self):
        """Interactive pattern learning system"""
        print("\n🎓 LEARNING MODE ACTIVATED")
        print("-" * 40)
        
        while True:
            pattern = input("Enter new phrase (or 'back' to return): ").strip().lower()
            
            if pattern == 'back':
                break
            
            if not pattern:
                print("❌ Please enter a valid phrase!")
                continue
            
            if pattern in self.dfas:
                print(f"❌ Pattern '{pattern}' already exists!")
                continue
            
            response = input("Enter response: ").strip()
            if not response:
                print("❌ Please enter a valid response!")
                continue
            
            category = input("Enter category (optional): ").strip() or "custom"
            
            # Generate DFA for new pattern
            dfa_states = self.generate_dfa(pattern)
            
            self.dfas[pattern] = {
                "dfa": dfa_states['states'],
                "accept": dfa_states['accept_state'],
                "responses": [response],
                "category": category,
                "priority": 3,
                "learned": True,
                "timestamp": datetime.now().isoformat()
            }
            
            print(f"✅ Successfully learned pattern: '{pattern}'")
            
            # Show DFA structure
            self.visualize_dfa(pattern)
            
            if input("Learn another pattern? (y/n): ").lower() != 'y':
                break
        
        if self.settings['auto_save']:
            self.save_custom_patterns()
    
    def generate_dfa(self, pattern):
        """Generate DFA states for a given pattern"""
        states = {}
        current_state = "q0"
        
        states[current_state] = {}
        
        for i, char in enumerate(pattern):
            next_state = f"q{i + 1}"
            states[current_state][char] = next_state
            states[next_state] = {}
            current_state = next_state
        
        return {
            'states': states,
            'accept_state': current_state
        }
    
    def visualize_dfa(self, pattern):
        """ASCII visualization of DFA structure"""
        if pattern not in self.dfas:
            print(f"❌ Pattern '{pattern}' not found!")
            return
        
        data = self.dfas[pattern]
        dfa = data['dfa']
        accept_state = data['accept']
        
        print(f"\n🔄 DFA Structure for '{pattern}':")
        print("-" * 50)
        print(f"📊 States: {len(dfa)}")
        print(f"🎯 Accept State: {accept_state}")
        print(f"📈 Category: {data.get('category', 'unknown')}")
        print("\n🔗 Transitions:")
        
        for state, transitions in dfa.items():
            if transitions:
                for char, next_state in transitions.items():
                    print(f"   {state} --['{char}']--> {next_state}")
            else:
                marker = " (ACCEPT)" if state == accept_state else " (DEAD)"
                print(f"   {state}{marker}")
        print("-" * 50)
    
    def show_statistics(self):
        """Display comprehensive conversation statistics"""
        print("\n📊 CONVERSATION STATISTICS")
        print("=" * 50)
        
        total = self.stats['total_messages']
        matched = self.stats['matched_messages']
        success_rate = (matched / total * 100) if total > 0 else 0
        
        print(f"💬 Total Messages: {total}")
        print(f"✅ Matched Messages: {matched}")
        print(f"📈 Success Rate: {success_rate:.1f}%")
        print(f"🕒 Session Duration: {datetime.now() - self.stats['session_start']}")
        print(f"🎯 Total Patterns: {len(self.dfas)}")
        
        if self.stats['pattern_usage']:
            print(f"\n🔥 Most Popular Patterns:")
            sorted_patterns = sorted(self.stats['pattern_usage'].items(), 
                                   key=lambda x: x[1], reverse=True)[:5]
            for i, (pattern, count) in enumerate(sorted_patterns, 1):
                print(f"   {i}. '{pattern}': {count} times")
        
        # Category analysis
        categories = defaultdict(int)
        for data in self.dfas.values():
            categories[data.get('category', 'unknown')] += 1
        
        print(f"\n📂 Pattern Categories:")
        for category, count in categories.items():
            print(f"   • {category}: {count} patterns")
        
        print("=" * 50)
    
    def list_patterns(self):
        """Display all available patterns organized by category"""
        print("\n📋 AVAILABLE PATTERNS")
        print("=" * 60)
        
        # Group patterns by category
        categories = defaultdict(list)
        for pattern, data in self.dfas.items():
            category = data.get('category', 'unknown')
            categories[category].append((pattern, data))
        
        for category, patterns in categories.items():
            print(f"\n🏷️  {category.upper()}:")
            print("-" * 30)
            
            for pattern, data in sorted(patterns):
                states_count = len(data['dfa'])
                usage = self.stats['pattern_usage'].get(pattern, 0)
                learned = "🎓" if data.get('learned') else ""
                
                print(f"   • '{pattern}' {learned}")
                print(f"     Response: {data['responses'][0][:50]}...")
                print(f"     States: {states_count} | Usage: {usage}x")
                print()
    
    def export_conversation(self):
        """Export conversation data to files"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Export chat history
        chat_filename = f"chat_history_{timestamp}.txt"
        with open(chat_filename, 'w', encoding='utf-8') as f:
            f.write("DFA CHATBOT CONVERSATION LOG\n")
            f.write("=" * 50 + "\n\n")
            
            for entry in self.stats['conversation_history']:
                f.write(f"{entry['timestamp']} - {entry['sender']}: {entry['message']}\n")
                if 'trace' in entry and entry['trace']:
                    f.write(f"   DFA Trace: {' → '.join(entry['trace'])}\n")
                f.write("\n")
            
            f.write("\nSTATISTICS:\n")
            f.write(f"Total Messages: {self.stats['total_messages']}\n")
            f.write(f"Matched Messages: {self.stats['matched_messages']}\n")
            success_rate = (self.stats['matched_messages'] / self.stats['total_messages'] * 100) if self.stats['total_messages'] > 0 else 0
            f.write(f"Success Rate: {success_rate:.1f}%\n")
        
        # Export DFA patterns
        patterns_filename = f"dfa_patterns_{timestamp}.json"
        with open(patterns_filename, 'w', encoding='utf-8') as f:
            json.dump(self.dfas, f, indent=2, ensure_ascii=False, default=str)
        
        print(f"✅ Exported:")
        print(f"   📄 Chat History: {chat_filename}")
        print(f"   🔧 DFA Patterns: {patterns_filename}")
    
    def save_custom_patterns(self):
        """Save user-learned patterns"""
        custom_patterns = {k: v for k, v in self.dfas.items() if v.get('learned')}
        
        if custom_patterns:
            with open('custom_patterns.json', 'w', encoding='utf-8') as f:
                json.dump(custom_patterns, f, indent=2, ensure_ascii=False, default=str)
            print(f"💾 Saved {len(custom_patterns)} custom patterns")
    
    def load_custom_patterns(self):
        """Load previously saved custom patterns"""
        try:
            if os.path.exists('custom_patterns.json'):
                with open('custom_patterns.json', 'r', encoding='utf-8') as f:
                    custom_patterns = json.load(f)
                    self.dfas.update(custom_patterns)
                print(f"📂 Loaded {len(custom_patterns)} custom patterns")
        except Exception as e:
            print(f"⚠️  Could not load custom patterns: {e}")
    
    def handle_command(self, user_input):
        """Handle special commands"""
        command = user_input.lower().strip()
        
        if command == 'help':
            self.print_welcome()
            return True
        elif command == 'stats':
            self.show_statistics()
            return True
        elif command == 'patterns':
            self.list_patterns()
            return True
        elif command == 'learn':
            self.learn_new_pattern()
            return True
        elif command == 'export':
            self.export_conversation()
            return True
        elif command == 'settings':
            self.modify_settings()
            return True
        elif command == 'clear':
            self.stats['conversation_history'].clear()
            print("🗑️  Conversation history cleared!")
            return True
        elif command.startswith('visualize '):
            pattern = command[10:]
            self.visualize_dfa(pattern)
            return True
        
        return False
    
    def modify_settings(self):
        """Interactive settings modification"""
        print("\n⚙️  SETTINGS")
        print("-" * 30)
        
        for key, value in self.settings.items():
            print(f"• {key}: {value}")
        
        print("\nModify setting (or 'back' to return):")
        setting = input("Setting name: ").strip()
        
        if setting == 'back' or setting not in self.settings:
            return
        
        if isinstance(self.settings[setting], bool):
            new_value = input(f"New value for {setting} (true/false): ").strip().lower()
            self.settings[setting] = new_value in ['true', 'yes', '1', 'on']
        else:
            new_value = input(f"New value for {setting}: ").strip()
            try:
                self.settings[setting] = float(new_value)
            except ValueError:
                self.settings[setting] = new_value
        
        print(f"✅ Updated {setting} to {self.settings[setting]}")
    
    def run(self):
        """Main chatbot loop"""
        while True:
            try:
                user_input = input("\n👤 You: ").strip()
                
                if user_input == "":
                    continue
                
                # Check for exit commands
                if user_input.lower() in ["exit", "quit", "bye", "end"]:
                    farewell_responses = [
                        "Goodbye! Thanks for chatting! 👋",
                        "See you later! Have a great day! 🌟",
                        "Farewell! Hope you enjoyed our DFA conversation! ✨"
                    ]
                    print(f"🤖 Bot: {random.choice(farewell_responses)}")
                    
                    if self.settings['auto_save']:
                        self.save_custom_patterns()
                    break
                
                # Handle special commands
                if self.handle_command(user_input):
                    continue
                
                # Update statistics
                self.stats['total_messages'] += 1
                
                # Find best match and generate response
                match_result = self.find_best_match(user_input)
                response, trace = self.generate_response(match_result, user_input)
                
                # Add response delay for more natural feel
                if self.settings['response_delay'] > 0:
                    time.sleep(self.settings['response_delay'])
                
                # Display response
                print(f"🤖 Bot: {response}")
                
                # Show DFA trace if enabled
                if self.settings['show_traces'] and trace:
                    print(f"🔍 DFA Trace: {' → '.join(trace)}")
                
                # Record conversation
                self.stats['conversation_history'].append({
                    'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'sender': 'User',
                    'message': user_input
                })
                self.stats['conversation_history'].append({
                    'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'sender': 'Bot',
                    'message': response,
                    'trace': trace if self.settings['show_traces'] else []
                })
                
            except KeyboardInterrupt:
                print(f"\n🤖 Bot: Goodbye! Thanks for the conversation! 👋")
                if self.settings['auto_save']:
                    self.save_custom_patterns()
                break
            except Exception as e:
                print(f"❌ Error: {e}")
                print("Please try again or type 'help' for commands.")

def main():
    """Main function to run the chatbot"""
    try:
        chatbot = AdvancedDFAChatbot()
        chatbot.run()
    except Exception as e:
        print(f"❌ Failed to start chatbot: {e}")

if __name__ == "__main__":
    main()