# React Hooks Quick Reference

> Print this out or keep it handy while coding!

**Last updated:** November 1, 2025

---

## 📋 State Hooks

### useState
```javascript
const [state, setState] = useState(initialValue);

// Functional update (when new state depends on old)
setState(prev => prev + 1);

// Lazy initialization (expensive computation)
const [state, setState] = useState(() => expensiveComputation());
```

**Use when:** Managing simple local state

---

### useReducer
```javascript
const [state, dispatch] = useReducer(reducer, initialState);

function reducer(state, action) {
  switch (action.type) {
    case 'INCREMENT':
      return { count: state.count + 1 };
    default:
      return state;
  }
}

// Dispatch actions
dispatch({ type: 'INCREMENT' });
dispatch({ type: 'UPDATE', payload: newValue });
```

**Use when:** Complex state logic, multiple sub-values

---

## 🔄 Effect Hooks

### useEffect
```javascript
// Run after every render
useEffect(() => {
  // Effect code
});

// Run once on mount
useEffect(() => {
  // Setup code
  return () => {
    // Cleanup code
  };
}, []);

// Run when dependencies change
useEffect(() => {
  // Effect code
}, [dep1, dep2]);
```

**Always cleanup:**
- ✅ Timers: `clearInterval`, `clearTimeout`
- ✅ Event listeners: `removeEventListener`
- ✅ Subscriptions: WebSocket close, unsubscribe
- ✅ Fetch requests: AbortController

---

### useLayoutEffect
```javascript
useLayoutEffect(() => {
  // Runs synchronously after DOM updates
  // but BEFORE browser paint
}, [deps]);
```

**Use when:** Need to read layout, prevent visual flicker

---

## 🌐 Context Hook

### useContext
```javascript
// 1. Create context
const ThemeContext = createContext('light');

// 2. Provide value
<ThemeContext.Provider value="dark">
  <App />
</ThemeContext.Provider>

// 3. Consume in any child
const theme = useContext(ThemeContext);
```

**Use when:** Avoiding prop drilling, global state

---

## 🔗 Ref Hook

### useRef
```javascript
// DOM access
const inputRef = useRef(null);
<input ref={inputRef} />
inputRef.current.focus();

// Storing mutable values (doesn't cause re-render)
const countRef = useRef(0);
countRef.current += 1;

// Previous value
const prevValue = useRef();
useEffect(() => {
  prevValue.current = value;
});
```

**Use when:** DOM manipulation, storing non-state values

---

## ⚡ Performance Hooks

### useMemo
```javascript
const memoizedValue = useMemo(() => {
  return expensiveComputation(a, b);
}, [a, b]);
```

**Use when:** Expensive calculations, prevent re-computation

---

### useCallback
```javascript
const memoizedCallback = useCallback(() => {
  doSomething(a, b);
}, [a, b]);
```

**Use when:** Passing callbacks to memoized components

---

### useTransition (React 18+)
```javascript
const [isPending, startTransition] = useTransition();

startTransition(() => {
  // Non-urgent state updates
  setSearchResults(hugeList.filter(...));
});

{isPending && <Spinner />}
```

**Use when:** Keep UI responsive during heavy updates

---

### useDeferredValue (React 18+)
```javascript
const deferredValue = useDeferredValue(value);

// Show stale value while new value is computing
<ExpensiveComponent value={deferredValue} />
```

**Use when:** Debouncing without external libraries

---

## 🎨 Custom Hooks

### Pattern
```javascript
function useCustomHook(param) {
  const [state, setState] = useState(null);

  useEffect(() => {
    // Logic using param
  }, [param]);

  return state; // or { state, helper functions }
}

// Usage
const value = useCustomHook(myParam);
```

### Common Custom Hooks

#### useLocalStorage
```javascript
function useLocalStorage(key, initialValue) {
  const [value, setValue] = useState(() => {
    const item = localStorage.getItem(key);
    return item ? JSON.parse(item) : initialValue;
  });

  useEffect(() => {
    localStorage.setItem(key, JSON.stringify(value));
  }, [key, value]);

  return [value, setValue];
}
```

#### useFetch
```javascript
function useFetch(url) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const controller = new AbortController();

    fetch(url, { signal: controller.signal })
      .then(res => res.json())
      .then(setData)
      .catch(setError)
      .finally(() => setLoading(false));

    return () => controller.abort();
  }, [url]);

  return { data, loading, error };
}
```

#### useToggle
```javascript
function useToggle(initialValue = false) {
  const [value, setValue] = useState(initialValue);
  const toggle = useCallback(() => setValue(v => !v), []);
  return [value, toggle];
}
```

---

## ⚠️ Rules of Hooks

### ✅ DO
- Call hooks at the **top level** of your function
- Call hooks from **React functions** (components or custom hooks)
- Name custom hooks with "use" prefix: `useMyHook`

### ❌ DON'T
```javascript
// ❌ Don't call in conditions
if (condition) {
  useState(0); // WRONG!
}

// ❌ Don't call in loops
for (let i = 0; i < 10; i++) {
  useEffect(() => {}); // WRONG!
}

// ❌ Don't call in regular functions
function regularFunction() {
  useState(0); // WRONG!
}
```

---

## 🐛 Common Pitfalls & Solutions

### Problem: State not updating immediately
```javascript
// ❌ WRONG
setCount(count + 1);
console.log(count); // Old value!

// ✅ CORRECT
setCount(prev => prev + 1); // Functional update
```

---

### Problem: Infinite loop
```javascript
// ❌ WRONG - Missing dependency
useEffect(() => {
  setCount(count + 1);
}); // No deps = runs every render!

// ✅ CORRECT
useEffect(() => {
  setCount(c => c + 1);
}, []); // Empty deps = runs once
```

---

### Problem: Stale closure
```javascript
// ❌ WRONG
useEffect(() => {
  const interval = setInterval(() => {
    setCount(count + 1); // Uses stale count!
  }, 1000);
  return () => clearInterval(interval);
}, []); // count not in deps!

// ✅ CORRECT
useEffect(() => {
  const interval = setInterval(() => {
    setCount(c => c + 1); // Functional update!
  }, 1000);
  return () => clearInterval(interval);
}, []);
```

---

### Problem: Memory leak
```javascript
// ❌ WRONG
useEffect(() => {
  const timer = setInterval(() => {}, 1000);
  // No cleanup!
}, []);

// ✅ CORRECT
useEffect(() => {
  const timer = setInterval(() => {}, 1000);
  return () => clearInterval(timer);
}, []);
```

---

## 🤔 Decision Trees

### When to use which state hook?

```
Is state simple and independent?
├─ YES → useState
└─ NO → Is it complex with multiple related values?
    ├─ YES → useReducer
    └─ NO → Need to share globally?
        ├─ YES → useContext (maybe + useReducer)
        └─ NO → useState is fine
```

### When to use useCallback/useMemo?

```
Is the component slow?
├─ NO → Don't optimize yet!
└─ YES → Profile with React DevTools
    ├─ Is computation expensive?
    │   └─ YES → Try useMemo
    └─ Passing callback to memoized child?
        └─ YES → Try useCallback
```

---

## 📊 Comparison Table

| Hook | Purpose | Returns | Common Use Case |
|------|---------|---------|-----------------|
| `useState` | Local state | `[state, setState]` | Form inputs, toggles |
| `useEffect` | Side effects | Cleanup function | API calls, subscriptions |
| `useContext` | Global state | Context value | Theme, auth, i18n |
| `useReducer` | Complex state | `[state, dispatch]` | Forms, shopping cart |
| `useRef` | Mutable value | Ref object | DOM access, timers |
| `useMemo` | Cache value | Memoized value | Expensive calculations |
| `useCallback` | Cache function | Memoized callback | Event handlers |

---

## 🔍 Debugging Checklist

When hooks behave unexpectedly:

- [ ] Check dependency arrays (use ESLint plugin!)
- [ ] Look for missing cleanup functions
- [ ] Verify you're not calling hooks conditionally
- [ ] Use React DevTools to inspect hook state
- [ ] Check for stale closures (missing deps)
- [ ] Ensure functional updates when state depends on previous
- [ ] Look for infinite loops (effect causing its own re-run)

---

## 🛠️ Essential Tools

- **ESLint Plugin**: `eslint-plugin-react-hooks`
- **React DevTools**: Browser extension
- **TypeScript**: Type safety for hooks

```bash
# Install ESLint plugin
npm install eslint-plugin-react-hooks --save-dev

# .eslintrc
{
  "plugins": ["react-hooks"],
  "rules": {
    "react-hooks/rules-of-hooks": "error",
    "react-hooks/exhaustive-deps": "warn"
  }
}
```

---

## 📚 Quick Links

- **Official Docs**: https://react.dev/reference/react/hooks
- **Rules of Hooks**: https://react.dev/warnings/invalid-hook-call-warning
- **Custom Hooks**: https://react.dev/learn/reusing-logic-with-custom-hooks

---

**Pro Tip:** Don't try to memorize everything. Understand the patterns, and refer back to this cheatsheet when needed!
