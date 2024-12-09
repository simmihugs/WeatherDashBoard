# WeatherDashBoard

I little weather dash board

## setup python
### setup env
```bash
python3 -m venv venv 
```

### activate env
```bash
source ./venv/bin/activate 
```

### install dep
```bash
pip install . 
```

## setup reflex
```bash
reflex init
```
### Pick option 0
```bash
╭[simmi@ccdev111] ~/Programs/WeatherDashBoard
╰─> reflex init                                                                                                                                           ✨🐱🏍🎉😎 (venv)  on branch main
────────────────────────────────────────────────────────────────────────────── Initializing WeatherDashBoard ───────────────────────────────────────────────────────────────────────────────
[17:15:07] Initializing the web directory.                                                                                                                                    console.py:104

Get started with a template:
(0) blank (https://blank-template.reflex.run) - A blank Reflex app.
(1) ai - Generate a template using AI [Experimental]
(2) choose templates - Choose an existing template.
Which template would you like to use? (0): 0
[17:15:24] Initializing the app directory.                                                                                                                                    console.py:104
Success: Initialized WeatherDashBoard using the blank template
╭[simmi@ccdev111] ~/Programs/WeatherDashBoard
╰─>
```

## run dev mode
```bash
reflex run --loglevel debug
```

