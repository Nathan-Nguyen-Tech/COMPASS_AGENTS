# React Hooks - 8-Week Study Guide

> From intermediate to advanced mastery

**Created:** November 1, 2025
**Source Materials:** [Research Brief](../../context/research/react/hooks-learning-resources.md)
**Target:** Intermediate React developers
**Time Commitment:** 1-2 hours/day

---

## Overview

**What you'll learn**: Master all React Hooks from useState to advanced performance optimization
**Prerequisites**: Basic React knowledge, comfortable with JavaScript ES6+
**Time estimate:** 8 weeks (56 days)
**Difficulty:** Intermediate → Advanced

## Learning Objectives

By completing this guide, you will be able to:
- ✅ Use all built-in React Hooks confidently in production code
- ✅ Choose the right hook for each scenario (useState vs useReducer vs useContext)
- ✅ Write custom hooks to extract reusable logic
- ✅ Prevent common pitfalls (memory leaks, stale closures, infinite loops)
- ✅ Optimize React performance using memoization hooks
- ✅ Debug hook-related issues efficiently

---

## 📅 Week 1-2: Foundation - State & Effects

### Week 1: useState Mastery

#### Day 1-2: useState Fundamentals
**📖 Read:**
- Official docs: https://react.dev/reference/react/useState
- GeeksforGeeks tutorial (sections 1-3)

**💻 Practice:**
```javascript
// Exercise 1: Simple Counter
// Build a counter with increment, decrement, reset

// Exercise 2: Form Input
// Create controlled form inputs for name, email, password

// Exercise 3: Toggle State
// Build a theme switcher (light/dark mode)
```

**🎯 Goal:** Understand state initialization, updating, and re-renders

#### Day 3-4: Functional Updates & Lazy Initialization

**📖 Read:**
- LogRocket Cheat Sheet: useState section
- Focus on functional updates pattern

**💻 Practice:**
```javascript
// Exercise 4: Counter with functional updates
const [count, setCount] = useState(0);
// Use: setCount(prev => prev + 1)

// Exercise 5: Expensive initialization
const [data, setData] = useState(() => {
  return computeExpensiveValue();
});
```

**🎯 Goal:** Master when and why to use functional updates

#### Day 5-7: useState Mini-Project

**🚀 Project: Todo List App**
Requirements:
- Add todos with text input
- Mark todos as complete/incomplete
- Delete todos
- Filter: All / Active / Completed
- Count of remaining todos

**Success Criteria:**
- All state managed with useState
- No prop drilling (keep it simple)
- Works without bugs

---

### Week 2: useEffect & Cleanup

#### Day 8-9: useEffect Basics

**📖 Read:**
- Official docs: https://react.dev/reference/react/useEffect
- GeeksforGeeks: useEffect section

**💻 Practice:**
```javascript
// Exercise 6: Document title updater
useEffect(() => {
  document.title = `Count: ${count}`;
}, [count]);

// Exercise 7: Data fetching
// Fetch user data from API on component mount
```

**🎯 Goal:** Understand dependency arrays and when effects run

#### Day 10-11: Cleanup Functions

**📖 Read:**
- LogRocket: Understanding useEffect Cleanup Function (full article)

**💻 Practice:**
```javascript
// Exercise 8: Timer with cleanup
useEffect(() => {
  const timer = setInterval(() => {}, 1000);
  return () => clearInterval(timer);
}, []);

// Exercise 9: Event listener cleanup
// Add window resize listener, cleanup on unmount
```

**🎯 Goal:** Prevent memory leaks with proper cleanup

#### Day 12-14: useEffect Project

**🚀 Project: Real-Time Clock + API Dashboard**

Part 1 - Clock:
- Display current time, updates every second
- Cleanup interval on unmount
- Format: HH:MM:SS

Part 2 - API Dashboard:
- Fetch data from public API (e.g., JSON Placeholder)
- Show loading state
- Handle errors gracefully
- Cleanup fetch on unmount (AbortController)

**Success Criteria:**
- No memory leaks
- Proper dependency arrays
- Clean separation of effects

---

## 📅 Week 3-4: Intermediate - Context & Reducers

### Week 3: useContext - Avoiding Prop Drilling

#### Day 15-16: Context Basics

**📖 Read:**
- Official docs: https://react.dev/reference/react/useContext
- Robin Wieruch article: Context section

**💻 Practice:**
```javascript
// Exercise 10: Theme Context
// Create ThemeContext, Provider, Consumer
// Toggle theme from any nested component

// Exercise 11: User Auth Context
// Simulate login/logout state shared globally
```

**🎯 Goal:** Understand when context solves real problems

#### Day 17-19: Context Patterns

**📖 Read:**
- Patterns.dev: Context patterns

**💻 Practice:**
- Create custom hook: `useTheme()`
- Optimize: Split contexts to prevent unnecessary re-renders
- Pattern: Context + useState for global state

**🚀 Mini-Project: Multi-Theme App**
- 3+ themes (light, dark, high-contrast)
- Language switcher (EN, VI)
- User preferences persist in localStorage
- Any component can access theme/language

---

### Week 4: useReducer - Complex State Logic

#### Day 20-22: useReducer Fundamentals

**📖 Read:**
- Official docs: https://react.dev/reference/react/useReducer
- Robin Wieruch: useState vs useReducer

**💻 Practice:**
```javascript
// Exercise 12: Counter with useReducer
const [state, dispatch] = useReducer(reducer, initialState);
// Actions: INCREMENT, DECREMENT, RESET

// Exercise 13: Form validation with useReducer
// Multiple fields with validation rules
```

**🎯 Goal:** Know when useReducer is better than useState

#### Day 23-25: useReducer + useContext

**📖 Read:**
- Pattern: Combine useReducer + useContext for powerful state management

**🚀 Project: Shopping Cart**
Requirements:
- Add/remove items
- Update quantities
- Calculate total price
- Apply discount codes

State Management:
- Use useReducer for cart logic
- Use useContext to share cart globally
- Actions: ADD_ITEM, REMOVE_ITEM, UPDATE_QUANTITY, APPLY_DISCOUNT

**Success Criteria:**
- Centralized state logic
- No prop drilling
- Predictable state updates

---

## 📅 Week 5-6: Advanced - Refs, Memoization & Custom Hooks

### Week 5: useRef & Performance Hooks

#### Day 26-28: useRef

**📖 Read:**
- Official docs: useRef
- Use cases: DOM access, storing mutable values

**💻 Practice:**
```javascript
// Exercise 14: Focus input on mount
const inputRef = useRef(null);
useEffect(() => {
  inputRef.current.focus();
}, []);

// Exercise 15: Previous value tracker
// Store previous state value without triggering re-render
```

#### Day 29-31: useMemo & useCallback

**📖 Read:**
- LogRocket: useMemo and useCallback best practices
- When NOT to use these hooks

**💻 Practice:**
```javascript
// Exercise 16: Expensive calculation with useMemo
const filtered = useMemo(() => {
  return items.filter(/* complex logic */);
}, [items, filters]);

// Exercise 17: Callback to memoized child
const handleClick = useCallback(() => {
  doSomething(value);
}, [value]);
```

**🎯 Goal:** Use memoization only when profiling shows it's needed

#### Day 32-35: Performance Project

**🚀 Project: Data Table with 10,000 Rows**
- Render large dataset
- Search/filter functionality
- Sort by columns
- Pagination

**Optimization Requirements:**
- Use useMemo for filtering/sorting
- Use useCallback for event handlers
- Measure before/after with React DevTools Profiler
- Implement virtualization (optional: react-window)

---

### Week 6: Custom Hooks

#### Day 36-38: Custom Hooks Fundamentals

**📖 Read:**
- Official: Reusing Logic with Custom Hooks
- Patterns.dev: Custom Hooks patterns

**💻 Practice:**
```javascript
// Exercise 18: useLocalStorage
function useLocalStorage(key, initialValue) {
  // Sync state with localStorage
}

// Exercise 19: useFetch
function useFetch(url) {
  // Return { data, loading, error }
}

// Exercise 20: useToggle
function useToggle(initialValue = false) {
  // Return [value, toggle]
}
```

#### Day 39-42: Custom Hooks Project

**🚀 Create 5 Reusable Custom Hooks:**

1. **useDebounce** - Debounce any value
2. **useForm** - Form state + validation
3. **useHover** - Detect hover state on any element
4. **useOnClickOutside** - Close modals/dropdowns
5. **useMediaQuery** - Responsive design helper

**Bonus Project:** Extract custom hooks from your previous projects

---

## 📅 Week 7-8: Expert Level - Production Patterns

### Week 7: React 18+ Features & Patterns

#### Day 43-45: Concurrent Features

**📖 Read:**
- useTransition
- useDeferredValue
- React 18 concurrent features

**💻 Practice:**
```javascript
// Exercise 21: useTransition for heavy updates
const [isPending, startTransition] = useTransition();
// Keep UI responsive during filtering

// Exercise 22: useDeferredValue
const deferredQuery = useDeferredValue(searchQuery);
// Show stale results while new ones load
```

#### Day 46-49: Advanced Patterns Project

**🚀 Project: Advanced Search Interface**
- Real-time search with 1000+ items
- Instant results preview
- Non-blocking UI updates
- Debounced search
- Highlighted results

**Use:**
- useTransition for responsive UI
- useDeferredValue for search
- useMemo for filtering
- Custom useDebounce hook

---

### Week 8: Production Ready & Best Practices

#### Day 50-52: Debugging & Error Patterns

**📖 Read:**
- React DevTools for hooks debugging
- Common mistakes and how to avoid them
- ESLint rules for hooks

**💻 Practice:**
- Install eslint-plugin-react-hooks
- Review all previous projects for violations
- Practice debugging with React DevTools

#### Day 53-56: Capstone Project

**🚀 Final Project: Complete Dashboard App**

Build a production-ready dashboard with:

**Features:**
- User authentication (fake API)
- Multiple pages/routes
- Data fetching from API
- Real-time updates
- Complex state management
- Performance optimized
- Responsive design
- Dark/light theme
- Form validation
- Error boundaries

**Hooks You Must Use:**
- useState, useEffect, useContext, useReducer
- useRef, useMemo, useCallback
- At least 3 custom hooks
- useTransition or useDeferredValue

**Success Criteria:**
- No ESLint hook violations
- No memory leaks
- Proper error handling
- Good performance (React DevTools Profiler)
- Clean, maintainable code
- Follows all best practices learned

---

## 📚 Recommended Resources Throughout

### Must-Read Articles
- [ ] LogRocket React Hooks Cheat Sheet
- [ ] Patterns.dev Hooks Pattern
- [ ] Robin Wieruch State Management guide
- [ ] LogRocket useEffect Cleanup article

### Video Courses (Choose One)
- [ ] Epic React by Kent C. Dodds (comprehensive)
- [ ] Scrimba Learn React (project-based)
- [ ] Net Ninja React Tutorial series (free)

### Tools
- [ ] Install React DevTools extension
- [ ] Setup ESLint with react-hooks plugin
- [ ] Use TypeScript (optional but recommended)

---

## 🎯 Assessment Checklist

After 8 weeks, you should be able to:

### Week 1-2 Skills
- [ ] Explain when to use functional updates in setState
- [ ] Write proper cleanup functions for all side effects
- [ ] Debug infinite loop issues with useEffect

### Week 3-4 Skills
- [ ] Choose between useState, useReducer, and useContext
- [ ] Implement global state without Redux
- [ ] Optimize context to prevent unnecessary re-renders

### Week 5-6 Skills
- [ ] Create custom hooks to extract reusable logic
- [ ] Use useMemo and useCallback appropriately (not everywhere!)
- [ ] Measure performance improvements with DevTools

### Week 7-8 Skills
- [ ] Use React 18 concurrent features
- [ ] Build production-ready apps following best practices
- [ ] Debug complex hook-related issues quickly

---

## 🚀 After Completing This Guide

### Immediate Next Steps
1. **Refactor old projects** - Apply new hook patterns
2. **Build portfolio projects** - Showcase your hook knowledge
3. **Read others' code** - Study open-source React projects
4. **Write blog posts** - Solidify learning by teaching

### Advanced Topics to Explore
- Server Components (Next.js 13+)
- React Query for data fetching
- Zustand or Jotai for state management
- Testing hooks with React Testing Library
- TypeScript with hooks

### Stay Updated
- Follow React blog: https://react.dev/blog
- React RFC discussions on GitHub
- Conference talks (React Conf, React Summit)

---

## 💡 Pro Tips

1. **Don't rush** - Take time to understand each concept deeply
2. **Build projects** - Theory is useless without practice
3. **Debug intentionally** - Break things to understand them
4. **Teach others** - Best way to solidify understanding
5. **Use TypeScript** - Catches many hook-related bugs early
6. **Profile before optimizing** - Don't use useMemo everywhere
7. **Read error messages** - React has great error messages for hooks
8. **Join communities** - React Discord, Reddit r/reactjs

---

**Good luck on your React Hooks mastery journey!** 🎉

Remember: The goal isn't to memorize APIs, but to understand the mental model of hooks and build intuition for when to use each one.

---

**Generated by:** Tech Learning Assistant
**Based on:** Curated research from official docs, expert tutorials, and best practices
**Last updated:** November 1, 2025
