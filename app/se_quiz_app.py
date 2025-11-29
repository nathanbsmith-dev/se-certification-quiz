"""
Systems Engineering Certification Quiz Application
A GUI-based quiz program with 300 questions, randomized presentation, and score tracking.
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import random
import re


class SEQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Systems Engineering Certification Quiz")
        self.root.geometry("900x700")
        
        # Quiz state
        self.all_questions = []
        self.current_question_index = 0
        self.score = 0
        self.answered_questions = []
        self.current_answer = None
        
        # Load questions from the markdown files
        self.load_questions()
        
        # Randomize question order
        random.shuffle(self.all_questions)
        
        # Create GUI
        self.create_widgets()
        
        # Display first question
        self.display_question()
    
    def load_questions(self):
        """Load all questions from the three exam files"""
        exam_files = [
            '/mnt/user-data/outputs/systems_engineering_practice_exam.md',
            '/mnt/user-data/outputs/systems_engineering_practice_exam_2.md',
            '/mnt/user-data/outputs/systems_engineering_practice_exam_3.md'
        ]
        
        for file_path in exam_files:
            self.parse_exam_file(file_path)
    
    def parse_exam_file(self, file_path):
        """Parse a markdown exam file to extract questions"""
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Split into questions section and answer key section
        parts = content.split('## ANSWER KEY WITH EXPLANATIONS')
        questions_part = parts[0]
        answer_key_part = parts[1] if len(parts) > 1 else ""
        
        # Parse answer key first
        answer_map = self.parse_answer_key(answer_key_part)
        
        # Split into sections
        sections = re.split(r'\n### Section \d+: (.+?) \(Questions \d+-\d+\)', questions_part)
        
        # Process each section
        for i in range(1, len(sections), 2):
            if i + 1 < len(sections):
                knowledge_area = sections[i].strip()
                section_content = sections[i + 1]
                
                # Extract questions from this section
                self.extract_questions_from_section(section_content, knowledge_area, answer_map)
    
    def parse_answer_key(self, answer_key_section):
        """Parse the answer key section to extract correct answers"""
        answer_map = {}
        # Match patterns like "**1. B**" or "**21. A**"
        pattern = r'\*\*(\d+)\.\s+([A-D])\*\*'
        matches = re.findall(pattern, answer_key_section)
        
        for question_num, answer in matches:
            answer_map[int(question_num)] = answer
        
        return answer_map
    
    def extract_questions_from_section(self, section_content, knowledge_area, answer_map):
        """Extract individual questions from a section"""
        # Split by question numbers
        question_blocks = re.split(r'\n\*\*(\d+)\.\*\*', section_content)
        
        for i in range(1, len(question_blocks), 2):
            if i + 1 >= len(question_blocks):
                continue
                
            question_num = int(question_blocks[i])
            block = question_blocks[i + 1]
            
            lines = block.strip().split('\n')
            if len(lines) < 5:
                continue
            
            # Extract question text
            question_text = lines[0].strip()
            
            # Extract options
            options = []
            for line in lines[1:]:
                line = line.strip()
                if line.startswith('- A)') or line.startswith('- B)') or line.startswith('- C)') or line.startswith('- D)'):
                    option_text = line[5:].strip()  # Remove "- X) "
                    options.append(option_text)
            
            if len(options) == 4 and question_num in answer_map:
                self.all_questions.append({
                    'question': question_text,
                    'options': options.copy(),
                    'correct_answer': answer_map[question_num],
                    'knowledge_area': knowledge_area,
                    'original_options': options.copy(),
                    'question_number': question_num
                })
    
    def create_widgets(self):
        """Create the GUI widgets"""
        # Top frame for progress and score
        top_frame = ttk.Frame(self.root, padding="10")
        top_frame.pack(fill=tk.X)
        
        self.progress_label = ttk.Label(top_frame, text="Question 1 of 300", font=('Arial', 12))
        self.progress_label.pack(side=tk.LEFT)
        
        self.score_label = ttk.Label(top_frame, text="Score: 0/0 (0%)", font=('Arial', 12))
        self.score_label.pack(side=tk.RIGHT)
        
        # Knowledge area label
        knowledge_frame = ttk.Frame(self.root, padding="5")
        knowledge_frame.pack(fill=tk.X)
        
        self.knowledge_label = ttk.Label(knowledge_frame, text="Knowledge Area: ", 
                                        font=('Arial', 10, 'italic'), foreground='blue')
        self.knowledge_label.pack()
        
        # Question frame
        question_frame = ttk.LabelFrame(self.root, text="Question", padding="15")
        question_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.question_text = scrolledtext.ScrolledText(question_frame, wrap=tk.WORD, 
                                                       height=6, font=('Arial', 11))
        self.question_text.pack(fill=tk.BOTH, expand=True)
        
        # Options frame
        options_frame = ttk.LabelFrame(self.root, text="Select Your Answer", padding="15")
        options_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.selected_option = tk.StringVar()
        self.option_buttons = []
        
        for i in range(4):
            rb = ttk.Radiobutton(options_frame, text="", variable=self.selected_option,
                               value=chr(65+i), command=self.on_option_selected)
            rb.pack(anchor=tk.W, pady=5)
            self.option_buttons.append(rb)
        
        # Feedback frame
        self.feedback_frame = ttk.Frame(self.root, padding="10")
        self.feedback_frame.pack(fill=tk.X, padx=10)
        
        self.feedback_label = ttk.Label(self.feedback_frame, text="", font=('Arial', 11, 'bold'))
        self.feedback_label.pack()
        
        # Buttons frame
        button_frame = ttk.Frame(self.root, padding="10")
        button_frame.pack(fill=tk.X)
        
        self.submit_button = ttk.Button(button_frame, text="Submit Answer", 
                                       command=self.submit_answer, state=tk.DISABLED)
        self.submit_button.pack(side=tk.LEFT, padx=5)
        
        self.next_button = ttk.Button(button_frame, text="Next Question", 
                                     command=self.next_question, state=tk.DISABLED)
        self.next_button.pack(side=tk.LEFT, padx=5)
        
        self.review_button = ttk.Button(button_frame, text="Review Answer", 
                                       command=self.review_answer, state=tk.DISABLED)
        self.review_button.pack(side=tk.LEFT, padx=5)
        
        ttk.Button(button_frame, text="Finish Quiz", 
                  command=self.finish_quiz).pack(side=tk.RIGHT, padx=5)
    
    def display_question(self):
        """Display the current question"""
        if self.current_question_index >= len(self.all_questions):
            self.finish_quiz()
            return
        
        question = self.all_questions[self.current_question_index]
        
        # Update progress
        self.progress_label.config(text=f"Question {self.current_question_index + 1} of {len(self.all_questions)}")
        self.knowledge_label.config(text=f"Knowledge Area: {question['knowledge_area']}")
        
        # Display question
        self.question_text.config(state=tk.NORMAL)
        self.question_text.delete(1.0, tk.END)
        self.question_text.insert(1.0, question['question'])
        self.question_text.config(state=tk.DISABLED)
        
        # Randomize options
        options_with_labels = list(zip(question['options'], ['A', 'B', 'C', 'D']))
        random.shuffle(options_with_labels)
        
        # Store the mapping for answer checking
        self.current_option_mapping = {}
        for i, (option_text, original_label) in enumerate(options_with_labels):
            display_label = chr(65 + i)  # A, B, C, D
            self.option_buttons[i].config(text=f"{display_label}) {option_text}")
            self.current_option_mapping[display_label] = original_label
        
        # Reset selection
        self.selected_option.set("")
        self.feedback_label.config(text="")
        self.submit_button.config(state=tk.DISABLED)
        self.next_button.config(state=tk.DISABLED)
        self.review_button.config(state=tk.DISABLED)
        
        # Enable option buttons
        for btn in self.option_buttons:
            btn.config(state=tk.NORMAL)
    
    def on_option_selected(self):
        """Enable submit button when an option is selected"""
        self.submit_button.config(state=tk.NORMAL)
    
    def submit_answer(self):
        """Check the submitted answer"""
        selected = self.selected_option.get()
        if not selected:
            return
        
        question = self.all_questions[self.current_question_index]
        
        # Map the selected display letter to the original option letter
        original_selected = self.current_option_mapping[selected]
        correct_answer = question['correct_answer']
        
        # Check if correct
        is_correct = (original_selected == correct_answer)
        
        # Store result
        self.answered_questions.append({
            'question': question,
            'selected': selected,
            'correct': is_correct,
            'mapping': self.current_option_mapping.copy()
        })
        
        if is_correct:
            self.score += 1
            self.feedback_label.config(text="✓ Correct!", foreground='green')
        else:
            # Find which display letter corresponds to the correct answer
            correct_display = [k for k, v in self.current_option_mapping.items() if v == correct_answer][0]
            self.feedback_label.config(text=f"✗ Incorrect. Correct answer: {correct_display}", foreground='red')
        
        # Update score
        total_answered = len(self.answered_questions)
        percentage = (self.score / total_answered * 100) if total_answered > 0 else 0
        self.score_label.config(text=f"Score: {self.score}/{total_answered} ({percentage:.1f}%)")
        
        # Disable submit and option buttons, enable next and review
        self.submit_button.config(state=tk.DISABLED)
        for btn in self.option_buttons:
            btn.config(state=tk.DISABLED)
        self.next_button.config(state=tk.NORMAL)
        self.review_button.config(state=tk.NORMAL)
    
    def next_question(self):
        """Move to the next question"""
        self.current_question_index += 1
        self.display_question()
    
    def review_answer(self):
        """Show detailed explanation for the current question"""
        if not self.answered_questions:
            return
        
        last_answered = self.answered_questions[-1]
        question = last_answered['question']
        
        # Find the correct answer text
        correct_idx = ord(question['correct_answer']) - 65
        correct_text = question['original_options'][correct_idx]
        
        # Create review window
        review_window = tk.Toplevel(self.root)
        review_window.title("Answer Review")
        review_window.geometry("600x400")
        
        # Question
        ttk.Label(review_window, text="Question:", font=('Arial', 11, 'bold')).pack(anchor=tk.W, padx=10, pady=5)
        q_text = scrolledtext.ScrolledText(review_window, wrap=tk.WORD, height=4, font=('Arial', 10))
        q_text.pack(fill=tk.X, padx=10, pady=5)
        q_text.insert(1.0, question['question'])
        q_text.config(state=tk.DISABLED)
        
        # Correct answer
        ttk.Label(review_window, text="Correct Answer:", font=('Arial', 11, 'bold')).pack(anchor=tk.W, padx=10, pady=5)
        ttk.Label(review_window, text=correct_text, font=('Arial', 10), 
                 wraplength=560, foreground='green').pack(anchor=tk.W, padx=20, pady=5)
        
        # Your answer
        if not last_answered['correct']:
            selected_display = last_answered['selected']
            selected_original = last_answered['mapping'][selected_display]
            selected_idx = ord(selected_original) - 65
            selected_text = question['original_options'][selected_idx]
            
            ttk.Label(review_window, text="Your Answer:", font=('Arial', 11, 'bold')).pack(anchor=tk.W, padx=10, pady=5)
            ttk.Label(review_window, text=selected_text, font=('Arial', 10), 
                     wraplength=560, foreground='red').pack(anchor=tk.W, padx=20, pady=5)
        
        ttk.Button(review_window, text="Close", command=review_window.destroy).pack(pady=10)
    
    def finish_quiz(self):
        """Show final results and exit options"""
        total = len(self.answered_questions)
        if total == 0:
            messagebox.showinfo("Quiz", "No questions answered yet!")
            return
        
        percentage = (self.score / total * 100)
        
        # Determine pass/fail (70% is common passing grade)
        passing_grade = 70
        passed = percentage >= passing_grade
        status = "PASSED ✓" if passed else "FAILED ✗"
        
        # Calculate knowledge area breakdown
        area_stats = {}
        for ans in self.answered_questions:
            area = ans['question']['knowledge_area']
            if area not in area_stats:
                area_stats[area] = {'correct': 0, 'total': 0}
            area_stats[area]['total'] += 1
            if ans['correct']:
                area_stats[area]['correct'] += 1
        
        # Create results window
        results_window = tk.Toplevel(self.root)
        results_window.title("Quiz Results")
        results_window.geometry("700x600")
        
        # Overall results
        ttk.Label(results_window, text="Quiz Complete!", font=('Arial', 16, 'bold')).pack(pady=10)
        
        status_color = 'green' if passed else 'red'
        ttk.Label(results_window, text=status, font=('Arial', 14, 'bold'), 
                 foreground=status_color).pack(pady=5)
        
        ttk.Label(results_window, text=f"Final Score: {self.score}/{total} ({percentage:.1f}%)", 
                 font=('Arial', 12)).pack(pady=5)
        ttk.Label(results_window, text=f"Passing Grade: {passing_grade}%", 
                 font=('Arial', 10)).pack(pady=2)
        
        # Knowledge area breakdown
        ttk.Label(results_window, text="\nPerformance by Knowledge Area:", 
                 font=('Arial', 12, 'bold')).pack(pady=10)
        
        # Scrollable frame for stats
        stats_frame = ttk.Frame(results_window)
        stats_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        canvas = tk.Canvas(stats_frame, height=300)
        scrollbar = ttk.Scrollbar(stats_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Add stats
        for area, stats in sorted(area_stats.items()):
            area_pct = (stats['correct'] / stats['total'] * 100) if stats['total'] > 0 else 0
            area_color = 'green' if area_pct >= passing_grade else 'orange' if area_pct >= 60 else 'red'
            
            area_frame = ttk.Frame(scrollable_frame)
            area_frame.pack(fill=tk.X, pady=5, padx=10)
            
            ttk.Label(area_frame, text=f"{area}:", font=('Arial', 10, 'bold')).pack(anchor=tk.W)
            ttk.Label(area_frame, text=f"{stats['correct']}/{stats['total']} ({area_pct:.1f}%)", 
                     font=('Arial', 10), foreground=area_color).pack(anchor=tk.W, padx=20)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Buttons
        button_frame = ttk.Frame(results_window)
        button_frame.pack(pady=10)
        
        ttk.Button(button_frame, text="Restart Quiz", 
                  command=lambda: [results_window.destroy(), self.restart_quiz()]).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Exit", 
                  command=self.root.quit).pack(side=tk.LEFT, padx=5)
    
    def restart_quiz(self):
        """Restart the quiz with new random order"""
        self.current_question_index = 0
        self.score = 0
        self.answered_questions = []
        random.shuffle(self.all_questions)
        self.display_question()
        self.score_label.config(text="Score: 0/0 (0%)")


def main():
    root = tk.Tk()
    app = SEQuizApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
