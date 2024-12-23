graph LR
  A[Start] --> B{Input a number}
  B --> C{Number is divisible by 2?}
  C -- Yes --> D[Print "Even"]
  C -- No --> E[Print "Odd"]
  D --> F[End]
  E --> F[End]
