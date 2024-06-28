from json import load, dump
e = {
    "insat --  المعهد الوطني للعلوم التطبيقية والتكنولوجيا بتونس": {
        "10520": {
            "i5tisas": "مرحلة تحضيرية مندمجة: رياضيات - فيزياء - إعالمـيـة - prepa",
            "a5er score bac info": 195.49,
            "formule": "FG+(M+SP+Algo)/3"}}}
with open("sa.json", "w")as f:
    dump(e, f )
with open("pas.json", "r") as f:
    t = load(f)

print(t)
