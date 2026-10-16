# Human blind ranking — stay-ambitious

You read replies from different systems for the same prompt and rank them **without knowing which system wrote which**. Replies are labelled only A, B, C, D, and the order is shuffled for every prompt.

You need Python 3 and a web browser. No internet connection or installs required.

## Step 1 — Build the page

Put the replies in `candidates.json` in this folder (use `candidates.example.json` as a model: each prompt has an `id`, the `prompt` text, a `source`, and `candidates` mapping a system name to its reply in Markdown). Then run:

```
cd evals/human
python3 build_ranking.py               # reads candidates.json
# or: python3 build_ranking.py candidates.example.json   (to try it out)
```

You get two files:

- `ranking.html` — the page you rank on. It has no system names in it.
- `key.json` — the answer key (which letter is which system). **Don't open this until you've finished ranking.**

Running it again on the same input gives the same shuffle. If a system name turns up anywhere in the page text (say a reply mentions "baseline"), the script prints a warning and exits with code 2. In that case, check before you start ranking.

## Step 2 — Rank

Double-click `ranking.html` to open it in your browser. It shows one prompt at a time ("3 of 10"):

1. **Rank** the replies best to worst. Drag the letters into the 1st/2nd/3rd… boxes, or click the *1st / 2nd / …* buttons under each reply.
2. For **each reply**, answer: *Would this make me ask for something bolder than I would have?* Yes / Somewhat / No.
3. Add a **note** if you want (optional).

Your answers save automatically in this browser, so you can close the tab and continue later. Use the same browser, and don't clear its site data. The numbered dots at the top turn green when a prompt is done and orange when it's only partly done. Click a dot to jump to that prompt.

Keyboard: Tab moves between buttons. Focus a letter and press 1–4 to place it, or 0 to un-rank it. Alt+←/→ moves to the previous or next prompt.

When you're done, click **Export results**. This downloads `results.json`. Move that file into this folder.

## Step 3 — See the scores

```
python3 score_ranking.py results.json key.json
```

This prints and saves `summary.md`. For each system it shows:

- **Mean rank** (1 = best)
- **% of prompts it came first**
- **% "Yes"** on the boldness question, plus % Yes or Somewhat
- A table for each prompt showing your ranking (with system names now revealed) and your notes

If `results.json` came from a different build of the page than `key.json`, the summary shows a warning. Rebuilding with different input or a different `--seed` changes the letters.

## Files

| File | What it is |
|---|---|
| `build_ranking.py` | Shuffles the replies and builds the page and key |
| `ranking_template.html` | Page design (used by the builder; don't open it directly) |
| `score_ranking.py` | Matches your results to the key and writes the summary |
| `candidates.example.json` | 2 sample prompts × 3 systems, for testing |
