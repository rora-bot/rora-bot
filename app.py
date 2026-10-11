from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Rora Bot</title>
<style>
body{font-family:Arial;background:#f0fdf4;margin:0;padding:15px}
h2{text-align:center;color:#15803d}
.chat{max-width:500px;margin:auto;background:white;border-radius:15px;padding:15px;box-shadow:0 4px 10px rgba(0,0,0,0.1)}
.msg{padding:10px 15px;border-radius:15px;margin:8px 0;max-width:80%}
.user{background:#dcfce7;margin-left:auto;text-align:right}
.bot{background:#f1f5f9}
input{width:75%;padding:12px;border-radius:20px;border:1px solid #ccc}
button{padding:12px 18px;border-radius:20px;border:none;background:#16a34a;color:white}
#box{height:400px;overflow-y:auto}
</style>
</head>
<body>
<h2>🧬 Rora FUHSI Biochemistry 2026 💚</h2>
<div class="chat">
<div id="box">
<div class="msg bot">Hi! I'm Rora Bot 💚 Ask me any Biochemistry question!</div>
</div>
<br>
<input id="q" placeholder="Type your question...">
<button onclick="ask()">Send</button>
</div>
<script>
async function ask(){
 let q=document.getElementById('q').value;
 if(!q) return;
 let box=document.getElementById('box');
 box.innerHTML+=`<div class='msg user'>${q}</div>`;
 document.getElementById('q').value='';
 let r=await fetch('/ask?q='+encodeURIComponent(q));
 let d=await r.text();
 box.innerHTML+=`<div class='msg bot'>${d}</div>`;
 box.scrollTop=box.scrollHeight;
}
</script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML)

@app.route('/ask')
def ask():
    q = request.args.get('q','').lower()
    if 'enzyme' in q:
        return "Enzymes are biological catalysts that speed up reactions. They are proteins (except ribozymes) and work by lowering activation energy. Example: Amylase breaks starch. 💚"
    if 'dna' in q or 'rna' in q:
        return "DNA is double-stranded, stores genetic info (A-T, G-C). RNA is single-stranded (A-U, G-C) and helps in protein synthesis. Central Dogma: DNA -> RNA -> Protein. 🧬"
    if 'protein' in q:
        return "Proteins are made of amino acids (20 types). 4 levels: Primary (sequence), Secondary (alpha/beta), Tertiary (3D), Quaternary (multiple subunits)."
    if 'glycolysis' in q:
        return "Glycolysis = 10 steps, in cytoplasm. Glucose (6C) -> 2 Pyruvate (3C). Net: 2 ATP + 2 NADH. Investment phase and Payoff phase."
    if 'krebs' in q or 'tca' in q or 'citric' in q:
        return "Krebs/TCA cycle: In mitochondria, Acetyl-CoA (2C) joins Oxaloacetate (4C) -> Citrate (6C). 1 cycle = 3 NADH, 1 FADH2, 1 GTP, 2 CO2. ~32 ATP total from glucose."
    return f"Good question about '{q}'! For FUHSI Biochemistry 2026, Rora is learning! Try asking about: enzyme, DNA, protein, glycolysis, Krebs cycle. 💚"

if __name__ == '__main__':
    app.run()
