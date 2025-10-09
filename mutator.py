**Mutator Tool — Canvas Guide**

---

### 1. Input Node

**Purpose:** Provide the base wordlist to mutate.

* Example file: `list.txt`
* One word per line (e.g., `hello`, `world`)

---

### 2. Mutation Options Node

**Purpose:** Configure transformations.

**Flags:**

* `-a / --append`: Add one or more suffixes

  * Example: `-a 2023 2024 2025!`
* `-p / --prepend`: Add one or more prefixes

  * Example: `-p admin user`
* `-H`: Convert to UPPERCASE
* `-L`: Convert to lowercase
* `-C`: Capitalize first letter
* `-r`: Reverse the word

---

### 3. Processing Node

**Purpose:** Combine all transformations.

* For each word in the input list:

  * Apply each prepend pattern (if any)
  * Apply each append pattern (if any)
  * Apply case transformations
  * Apply reversing if specified

---

### 4. Output Node

**Purpose:** Save final results.

* Use `-o` to specify output file

  * Example: `-o mutated.txt`
* Each mutation is written on a new line

---

### 5. Example Flow

**Command:**

```
./mutator.py -w list.txt -o out.txt -a 2023 2024! -p admin user -H
```

**Result:**

```
ADMINHELLO2023
ADMINHELLO2024!
USERHELLO2023
USERHELLO2024!
ADMINWORLD2023
ADMINWORLD2024!
USERWORLD2023
USERWORLD2024!
```

---

### 6. Expansion Ideas Node

**Possible future upgrades:**

* Support numeric ranges (e.g., `-a 2020-2025`)
* Add leetspeak mode (`--leet`)
* Add random separators (`--sep - _ .`)
* Combine multiple wordlists (`--combine list1.txt list2.txt`)
