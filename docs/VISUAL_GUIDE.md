# Systems Engineering Quiz Application - Visual Guide

## Application Interface Overview

### Main Window Layout

```
┌─────────────────────────────────────────────────────────────────────────┐
│ Systems Engineering Certification Quiz                                  │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  Question 1 of 300                                  Score: 0/0 (0%)    │
│                                                                          │
│  Knowledge Area: Systems Engineering Fundamentals                       │
│                                                                          │
│  ┌─ Question ─────────────────────────────────────────────────────────┐ │
│  │                                                                     │ │
│  │  What is the primary purpose of systems engineering?               │ │
│  │                                                                     │ │
│  │                                                                     │ │
│  │                                                                     │ │
│  └─────────────────────────────────────────────────────────────────────┘ │
│                                                                          │
│  ┌─ Select Your Answer ──────────────────────────────────────────────┐ │
│  │                                                                     │ │
│  │  ○ A) To design individual components                              │ │
│  │                                                                     │ │
│  │  ○ B) To reduce project costs only                                 │ │
│  │                                                                     │ │
│  │  ○ C) To integrate and manage complex systems throughout their     │ │
│  │       lifecycle                                                     │ │
│  │                                                                     │ │
│  │  ○ D) To create software applications                              │ │
│  │                                                                     │ │
│  └─────────────────────────────────────────────────────────────────────┘ │
│                                                                          │
│  [Feedback area - appears after submission]                            │
│                                                                          │
│  [ Submit Answer ]  [ Next Question ]  [ Review Answer ]  [ Finish Quiz ]│
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## Feature Demonstrations

### 1. Question Display
- **Progress Tracker**: Shows current question number out of 300
- **Score Display**: Real-time score with percentage
- **Knowledge Area**: Displays the SE topic for each question
- **Scrollable Text**: Long questions can be scrolled
- **Randomized Options**: A, B, C, D positions change for each question

### 2. Answer Selection Flow

**Step 1: Initial State**
```
[ Submit Answer ] ← Disabled until option selected
[ Next Question ] ← Disabled
[ Review Answer ] ← Disabled
```

**Step 2: After Selecting an Option**
```
● C) To integrate and manage complex systems... ← Selected
[ Submit Answer ] ← Now ENABLED
```

**Step 3: After Submitting**
```
✓ Correct!  (shown in green)
   or
✗ Incorrect. Correct answer: C  (shown in red)

[ Submit Answer ] ← Disabled
[ Next Question ] ← ENABLED
[ Review Answer ] ← ENABLED
```

### 3. Review Answer Window

```
┌─────────────────────────────────────────────────────────────┐
│ Answer Review                                                │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Question:                                                   │
│  ┌────────────────────────────────────────────────────────┐ │
│  │ What is the primary purpose of systems engineering?    │ │
│  └────────────────────────────────────────────────────────┘ │
│                                                              │
│  Correct Answer:                                            │
│  To integrate and manage complex systems throughout their   │
│  lifecycle                                                   │
│                                                              │
│  Your Answer: (if incorrect)                                │
│  To design individual components                            │
│                                                              │
│                    [ Close ]                                 │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### 4. Final Results Window

```
┌─────────────────────────────────────────────────────────────┐
│ Quiz Results                                                 │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│                    Quiz Complete!                            │
│                                                              │
│                     PASSED ✓                                 │
│                   (or FAILED ✗)                              │
│                                                              │
│            Final Score: 245/300 (81.7%)                     │
│              Passing Grade: 70%                              │
│                                                              │
│         Performance by Knowledge Area:                       │
│  ┌────────────────────────────────────────────────────────┐ │
│  │                                                         │ │
│  │ Systems Engineering Fundamentals:                      │ │
│  │   16/20 (80.0%)                                        │ │
│  │                                                         │ │
│  │ Requirements Engineering:                               │ │
│  │   12/15 (80.0%)                                        │ │
│  │                                                         │ │
│  │ System Architecture and Design:                        │ │
│  │   11/15 (73.3%)                                        │ │
│  │                                                         │ │
│  │ Integration, Verification & Validation:                │ │
│  │   13/15 (86.7%)                                        │ │
│  │                                                         │ │
│  │ Risk Management:                                        │ │
│  │   8/10 (80.0%)                                         │ │
│  │                                                         │ │
│  │ [... more knowledge areas ...]                         │ │
│  │                                                         │ │
│  └────────────────────────────────────────────────────────┘ │
│                                                              │
│         [ Restart Quiz ]           [ Exit ]                  │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

## Color Coding

- **Green Text**: Correct answer feedback
- **Red Text**: Incorrect answer feedback
- **Blue Text**: Knowledge area labels
- **Orange/Red in Results**: Knowledge areas below passing threshold
- **Green in Results**: Knowledge areas meeting/exceeding passing threshold

## Button States

### Submit Answer
- **Disabled**: When no option is selected or after already submitted
- **Enabled**: When an option is selected and not yet submitted

### Next Question
- **Disabled**: Before submitting an answer
- **Enabled**: After submitting an answer

### Review Answer
- **Disabled**: Before submitting an answer
- **Enabled**: After submitting an answer

### Finish Quiz
- **Always Enabled**: Can view results at any time

## Usage Workflow

```
START
  │
  ├─→ Load 300 questions
  │
  ├─→ Randomize order
  │
  ├─→ Display Question 1
  │
  └─→ [USER INTERACTION LOOP]
       │
       ├─→ Select answer → Enable Submit
       │
       ├─→ Submit → Show feedback
       │
       ├─→ (Optional) Review Answer → View explanation
       │
       ├─→ Next Question → Load next random question
       │
       └─→ Repeat until Finish Quiz clicked
             │
             └─→ Show Results
                  │
                  ├─→ Overall Score
                  ├─→ Pass/Fail Status
                  ├─→ Knowledge Area Breakdown
                  │
                  └─→ [Restart] or [Exit]
```

## Example Session

**Question 1**
- Topic: Systems Engineering Fundamentals
- Status: Answered Correctly ✓
- Score: 1/1 (100%)

**Question 2**
- Topic: Requirements Engineering
- Status: Answered Incorrectly ✗
- Score: 1/2 (50%)

**Question 3**
- Topic: System Architecture
- Status: Answered Correctly ✓
- Score: 2/3 (66.7%)

... continues through 300 questions ...

**Final Results**
- Total Score: 245/300 (81.7%)
- Status: PASSED ✓
- Weakest Area: Risk Management (65%)
- Strongest Area: Integration & Testing (95%)

## Tips for Using the Interface

1. **Read Carefully**: Take time to read each question fully
2. **Check Knowledge Area**: Note which topics need more study
3. **Use Review**: Learn from explanations, don't just move on
4. **Track Progress**: Watch your percentage improve over time
5. **Finish Strategically**: Don't rush to "Finish Quiz" - complete all 300
6. **Restart for Practice**: Each restart gives a new random order

## Keyboard Navigation

While the application primarily uses mouse interaction:
- Click radio buttons to select answers
- Click buttons to submit, review, or advance
- Use mouse wheel to scroll long questions

## Performance Indicators

### During Quiz
- **Green Score**: Trending toward pass
- **Yellow Score**: Borderline (68-72%)
- **Red Score**: Below passing

### In Results
- **Green Knowledge Areas**: ≥ 70%
- **Orange Knowledge Areas**: 60-69%
- **Red Knowledge Areas**: < 60%

---

This visual guide provides an overview of the application interface and workflow. 
The actual application is fully interactive and provides immediate feedback as you practice.
