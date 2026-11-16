# -*- coding: utf-8 -*-
"""Construiește cele DOUĂ pluginuri Archa-ai din aceeași sursă (16 nov 2026, Cristian: „avem două tipuri de plugin,
cele de pe marketuri și cele complete de pe site... autoupdate neapărat”).

- `plugins/archa-ai`          = SURSA: pluginul pentru directoare (conectorul pe ușa /plugin, fără randări).
- `plugins/archa-ai-complet`  = GENERAT de aici: aceleași reguli (skill-ul), conectorul pe ușa /complet (toate
                                uneltele, cu randările). Nu se editează de mână.
- `.claude-plugin/marketplace.json` = catalogul cu AMÂNDOUĂ, ca să se actualizeze singure din GitHub.

Actualizarea automată (documentația Claude, citită pe 16 nov 2026) vine DOAR din catalogul Git, cu „Enable
auto-update” (Claude Code) sau „Sync automatically” (claude.ai / Cowork), și numai când crește `version` din
plugin.json — de aceea versiunea e una singură, aici, pentru ambele. Arhivele .zip de pe site nu se actualizează
singure: rămân rezervă pentru cine nu poate adăuga catalogul.

    python -I scripturi/construieste.py 0.2.3 [--site K:/archa-mcp/mcp/addon/claude]
"""
import argparse
import json
import pathlib
import re
import shutil
import zipfile

RAD = pathlib.Path(__file__).resolve().parent.parent
SURSA = RAD / "plugins" / "archa-ai"
COMPLET = RAD / "plugins" / "archa-ai-complet"
BAZA_MCP = "https://mcp.archa-ai.ro"


def _json(cale, d):
    cale.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def construieste(versiune: str) -> None:
    if not re.fullmatch(r"\d+\.\d+\.\d+", versiune):
        raise SystemExit("versiunea e X.Y.Z")
    # 1. sursa: versiunea
    p = json.loads((SURSA / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
    p["version"] = versiune
    _json(SURSA / ".claude-plugin" / "plugin.json", p)
    # 2. varianta completă: copia sursei, cu numele, descrierea și ușa ei
    if COMPLET.exists():
        shutil.rmtree(COMPLET)
    shutil.copytree(SURSA, COMPLET)
    c = dict(p, name="archa-ai-complet", displayName="Archa-ai complet (cu randări)",
             description=p["description"].rstrip(".") + ". Varianta completă: conectorul cu toate uneltele Archa-ai, "
                         "inclusiv randările și editarea imaginilor.")
    _json(COMPLET / ".claude-plugin" / "plugin.json", c)
    _json(COMPLET / ".mcp.json", {"mcpServers": {"archa-ai": {"type": "http", "url": BAZA_MCP + "/complet"}}})
    readme = (SURSA / "README.md").read_text(encoding="utf-8")
    readme = readme.replace(BAZA_MCP + "/plugin", BAZA_MCP + "/complet").replace(
        "# Archa-ai\n", "# Archa-ai complet (cu randări)\n\nAceleași reguli ca pluginul „Archa-ai”, cu conectorul "
                        "complet: toate uneltele, inclusiv randările. Instalează-l pe UNUL dintre ele, nu pe amândouă.\n",
        1).replace("install archa-ai --marketplace", "install archa-ai-complet --marketplace")
    (COMPLET / "README.md").write_text(readme, encoding="utf-8", newline="\n")
    # 3. catalogul, cu amândouă
    m = json.loads((RAD / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8"))
    baza = next(x for x in m["plugins"] if x["name"] == "archa-ai")
    m["plugins"] = [baza, {"name": "archa-ai-complet", "source": "./plugins/archa-ai-complet",
                           "description": "Aceleași reguli ca „archa-ai”, cu conectorul complet (toate uneltele, "
                                          "inclusiv randările). Instalează unul singur dintre cele două."}]
    _json(RAD / ".claude-plugin" / "marketplace.json", m)
    print("construit %s: archa-ai si archa-ai-complet" % versiune)


def arhive(versiune: str, site: pathlib.Path | None) -> None:
    dist = RAD / "dist"
    dist.mkdir(exist_ok=True)
    for dosar in (SURSA, COMPLET):
        z = dist / ("%s.zip" % dosar.name)
        with zipfile.ZipFile(z, "w", zipfile.ZIP_DEFLATED) as zf:
            for f in sorted(dosar.rglob("*")):
                if f.is_file():
                    zf.write(f, "%s/%s" % (dosar.name, f.relative_to(dosar).as_posix()))
        print("arhiva", z.name, z.stat().st_size)
        if site:
            shutil.copy2(z, site / z.name)
    if site:
        (site / "VERSIUNE").write_text(versiune + "\n", encoding="utf-8", newline="\n")
        print("puse pe site in", site)


if __name__ == "__main__":
    a = argparse.ArgumentParser()
    a.add_argument("versiune")
    a.add_argument("--site", type=pathlib.Path)
    arg = a.parse_args()
    construieste(arg.versiune)
    arhive(arg.versiune, arg.site)
