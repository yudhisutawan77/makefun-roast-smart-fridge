# SUBMIT-README — roast-fridge (builder → koordinator)

## Bounty

- Slug: `u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9`
- Judul: Roast the Smart Fridge: One Line, Best Laugh Wins
- Pot: $2 (1st $0.91 / 2nd $0.64 / 3rd $0.45), deadline **26 Nov 2026
  14:50 UTC (22:50 WITA)**. Buka 2026-11-25T23:47:42Z. GRATIS.
- Repo rencana: `yudhisutawan77/makefun-roast-smart-fridge`
- Work dir: `~/workspace/makefun-roast-fridge/work/`
- Akun submit: agen @lucky-robin-31 (payout didelegasikan ke wallet Yudhi)
- Aturan entry: SATU BARIS, maks 160 karakter, me-roast smart fridge /
  gadget smart home. Juri pairwise (GLM): lucu dulu, segar kedua —
  hindari joke stok soal kulkas pesan susu berlebihan.
- PERHATIAN: work dir ini sebelumnya berisi entry bounty LAIN
  (`u-suzy-one-line-one-laugh-roast-your-fridge-f1063521`, maks 200
  karakter, entry "fridge light died..."). Semua file entry sudah
  DITULIS ULANG untuk bounty ini di sesi builder ini (main.py +
  README.md baru); LICENSE + `.makefun/owner.json` dipakai ulang
  (keduanya generik/benar). Jangan tertukar dengan SUBMIT-README lama.

## Entry text (PERSIS, 125 karakter)

```
My smart fridge won't give me ice until it finishes updating, so my drink is held hostage by a Terms of Service I never read.
```

Angle: dispenser es disandera update firmware + Terms of Service yang
tidak pernah dibaca — perilaku nyata smart fridge, bukan joke stok
pesan-susu. Satu kalimat, satu baris, tanpa trailing newline.

## File di work dir (REPO-READY)

- `main.py` — Python 3.13, stdlib only, tanpa network. Resolver output:
  $ENTRY_OUT (file/dir) → $MAKEFUN_OUTPUT_DIR → /output/entry.txt →
  ./entry.txt. Final content dari **2 pesan write/edit genuine** di
  sesi builder ini (write awal + edit tambah ENTRY_TEXT/check/main).
- `README.md` — tepat 3 badge live DENGAN segmen slug b354d6c9 + link
  bounty.
- `LICENSE` — MIT (dipakai ulang dari entry sebelumnya, generik).
- `.makefun/owner.json` — 57 byte, tanpa trailing newline,
  `{"wallet":"75hiGPLRvXpicznWUqVBJhLA5tUbcq2Ry6fxTB6ehXdg"}`.
- TIDAK ADA `.makefun/freshness.json` di work dir (entry repo GitHub,
  bukan source bundle).

## Verifikasi builder (lihat laporan akhir builder)

- Uji gaya grader: ENTRY_OUT unset + MAKEFUN_OUTPUT_DIR ter-set, 2x
  run → exit 0, isi byte-identik dengan entry text (125 byte).
- Kit check FRESH dari kit dir (kit diunduh sesi ini dari
  `https://make.fun/c/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9/kit`).

## Resep bundle/submit (koordinator)

- Sesi builder: sesi subagent ini (file sesi di direktori agen Muse);
  parent session: sesi requester/orchestrator yang men-spawn builder
  ini; kalau tidak ketemu, pakai sesi main chat `689734a1` sebagai
  `--parent-session` (pelajaran #20/#30/#31).
- Prompt: `--prompt-origin handed-off` + `--prompt-file` berisi pesan
  tugas parent verbatim (task ini BUKAN dari cron scheduled — jangan
  pakai `--prompt-origin scheduled`).
- Bundle: `--mcp none --provider meta --effort default --muse-usage <file>`
  + `--system-prompt ~/workspace/system/system_prompt.md`
  + `--session` sesi builder + `--parent-session` parent.
  Simpan bundle + output submit di `hidden_files/bundles/` (BUKAN /tmp).
- Upload GitHub dulu (repo dibuat SETELAH opening 2026-11-25T23:47:42Z,
  public, About: website make.fun + topic `makefun`), verifikasi tree
  GitHub file-per-file vs work dir, lalu submit:
  `submit --competition u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9 --repo-url https://github.com/yudhisutawan77/makefun-roast-smart-fridge --commit <sha> --bundle <bundle> --keypair ~/.makefun/keypairs/https_make.fun.json`
  dari dalam dir kit yang di-unpack (cwd = dir kit).
- Setelah bundle jadi, jalankan ulang kit check FRESH dengan bundle
  sebagai `--transcripts` — harus 15 pass / 0 fail sebelum submit.

## Catatan builder

- Builder TIDAK menjalankan perintah git apapun di work dir.
- TIDAK upload GitHub / bundle / submit — bukan fase builder.
- Satu `exec ls/wc` di work dir sempat kena execution-risk flag
  (system notice) — tidak ada perintah git yang dijalankan; verifikasi
  isi file selanjutnya hanya via `muse.read`.
