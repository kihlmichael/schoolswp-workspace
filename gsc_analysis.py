#!/usr/bin/env python3
import csv, os
from datetime import datetime, timedelta
from collections import defaultdict

BASE = os.path.join(chr(99)+chr(58)+os.sep,"Users","micha","Desktop","https___schoolswp.com_-Performance-on-Search-2026-02-06")

def open_csv(fn):
    fs = os.listdir(BASE)
    m = None
    for x in fs:
        if fn=="Requetes" and x.startswith("Requ") and x.endswith(".csv"): m=x; break
        elif fn=="Graphique" and x.startswith("Graph") and x.endswith(".csv"): m=x; break
        elif fn=="Pages" and x.startswith("Pages") and x.endswith(".csv"): m=x; break
    if m is None: m=fn+".csv"
    p = os.path.join(BASE, m)
    for e in ("utf-8","latin-1","cp1252"):
        try:
            fh = open(p, encoding=e, newline="")
            fh.read(1); fh.seek(0); return fh
        except: continue
    raise RuntimeError("Cannot decode "+p)

def pctr(v): return float(str(v).strip().replace("%","").replace(",","."))
def pf(v): return float(str(v).strip().replace(",","."))
def pint(v): return int(float(str(v).strip().replace(",","").replace(chr(160),"")))
def fm(n):
    if isinstance(n,float): return "{:,.2f}".format(n)
    return "{:,}".format(n)

def hdr(t):
    print(); print("="*90); print("  "+t); print("="*90)

def shdr(t):
    print(); print("--- "+t+" ---")

def analyze_graphique():
    hdr("1. GRAPHIQUE.CSV - Monthly totals + period comparison")
    fh = open_csv("Graphique")
    reader = csv.DictReader(fh)
    rows = []
    monthly = defaultdict(lambda: {"c":0,"i":0,"ps":0.0,"d":0})
    for r in reader:
        dt = datetime.strptime(r["Date"],"%Y-%m-%d")
        c = pint(r["Clics"])
        im = pint(r["Impressions"])
        p = pf(r["Position"])
        rows.append({"date":dt,"clicks":c,"impressions":im,"position":p})
        k = dt.strftime("%Y-%m")
        monthly[k]["c"] += c
        monthly[k]["i"] += im
        monthly[k]["ps"] += p
        monthly[k]["d"] += 1
    fh.close()
    shdr("Monthly totals")
    print("{:<12} {:>10} {:>14} {:>14} {:>6}".format("Month","Clicks","Impressions","Avg Position","Days"))
    print("-"*60)
    for m in sorted(monthly.keys()):
        d = monthly[m]
        ap = d["ps"]/d["d"]
        print("{:<12} {:>10} {:>14} {:>14.2f} {:>6}".format(m,fm(d["c"]),fm(d["i"]),ap,d["d"]))
    tc=sum(d["c"] for d in monthly.values())
    ti=sum(d["i"] for d in monthly.values())
    td=sum(d["d"] for d in monthly.values())
    tp=sum(d["ps"] for d in monthly.values())/td
    print("-"*60)
    print("{:<12} {:>10} {:>14} {:>14.2f} {:>6}".format("TOTAL",fm(tc),fm(ti),tp,td))
    shdr("Period comparison: Last 30 days vs Prior 30 days")
    rows.sort(key=lambda x: x["date"])
    latest = rows[-1]["date"]
    cut30 = latest - timedelta(days=29)
    cut60 = cut30 - timedelta(days=30)
    last30 = [r for r in rows if r["date"] >= cut30]
    prior30 = [r for r in rows if cut60 <= r["date"] < cut30]
    def pstats(pr):
        if not pr: return 0,0,0
        return sum(r["clicks"] for r in pr), sum(r["impressions"] for r in pr), sum(r["position"] for r in pr)/len(pr)
    lc,li,lp = pstats(last30)
    pc,pi,pp = pstats(prior30)
    def dpct(n,o):
        if o==0: return "N/A"
        pct=(n-o)/o*100; s="+" if pct>=0 else ""
        return "{}{:.1f}%".format(s,pct)
    def dabs(n,o):
        d=n-o; s="+" if d>=0 else ""
        return "{}{}".format(s,fm(d))
    ls=min(r["date"] for r in last30).strftime("%Y-%m-%d")
    le=max(r["date"] for r in last30).strftime("%Y-%m-%d")
    ps2=min(r["date"] for r in prior30).strftime("%Y-%m-%d") if prior30 else "N/A"
    pe=max(r["date"] for r in prior30).strftime("%Y-%m-%d") if prior30 else "N/A"
    print("  Last 30 days : {} to {}  ({} days)".format(ls,le,len(last30)))
    print("  Prior 30 days: {} to {}  ({} days)".format(ps2,pe,len(prior30)))
    print()
    print("{:<16} {:>12} {:>12} {:>12} {:>10}".format("Metric","Last 30d","Prior 30d","Change","Change %"))
    print("-"*66)
    print("{:<16} {:>12} {:>12} {:>12} {:>10}".format("Clicks",fm(lc),fm(pc),dabs(lc,pc),dpct(lc,pc)))
    print("{:<16} {:>12} {:>12} {:>12} {:>10}".format("Impressions",fm(li),fm(pi),dabs(li,pi),dpct(li,pi)))
    pd2=lp-pp; ps3="+" if pd2>=0 else ""
    print("{:<16} {:>12.2f} {:>12.2f} {}{:>11.2f} {:>10}".format("Avg Position",lp,pp,ps3,pd2,"(lower=better)"))

def analyze_requetes():
    hdr("2. REQUETES.CSV - Query analysis")
    fh = open_csv("Requetes")
    reader = csv.DictReader(fh)
    qcol = reader.fieldnames[0]
    queries = []
    for r in reader:
        queries.append({"query":r[qcol],"clicks":pint(r["Clics"]),"impressions":pint(r["Impressions"]),"ctr":pctr(r["CTR"]),"position":pf(r["Position"])})
    fh.close()
    print("  Total queries loaded: {}".format(len(queries)))
    shdr("2a. CTR Opportunities (position <= 10, CTR < 2%) - Top 20 by impressions")
    print("    Ranking well but few clicks. Improve titles and meta descriptions.")
    print()
    opps = sorted([q for q in queries if q["position"]<=10 and q["ctr"]<2.0], key=lambda x:x["impressions"], reverse=True)
    print("{:<4} {:<50} {:>7} {:>8} {:>7} {:>7}".format("#","Query","Clicks","Impr","CTR","Pos"))
    print("-"*87)
    for i,q in enumerate(opps[:20],1):
        print("{:<4} {:<50} {:>7,} {:>8,} {:>6.2f}% {:>7.2f}".format(i,q["query"][:48],q["clicks"],q["impressions"],q["ctr"],q["position"]))
    print("  ({} total queries match)".format(len(opps)))
    shdr("2b. Striking Distance (position 4-15, impressions > 200) - Top 20 by impressions")
    print("    Close to top 3. Minor optimization can push these up.")
    print()
    sd = sorted([q for q in queries if 4<=q["position"]<=15 and q["impressions"]>200], key=lambda x:x["impressions"], reverse=True)
    print("{:<4} {:<50} {:>7} {:>8} {:>7} {:>7}".format("#","Query","Clicks","Impr","CTR","Pos"))
    print("-"*87)
    for i,q in enumerate(sd[:20],1):
        print("{:<4} {:<50} {:>7,} {:>8,} {:>6.2f}% {:>7.2f}".format(i,q["query"][:48],q["clicks"],q["impressions"],q["ctr"],q["position"]))
    print("  ({} total queries match)".format(len(sd)))
    shdr("2c. Content to Create (position > 20, impressions > 500) - Top 20 by impressions")
    print("    High demand, poor ranking. Dedicate content to these topics.")
    print()
    tc = sorted([q for q in queries if q["position"]>20 and q["impressions"]>500], key=lambda x:x["impressions"], reverse=True)
    if not tc:
        print("  No queries match (pos>20 AND impr>500). Relaxing to impr>100:")
        print()
        tc = sorted([q for q in queries if q["position"]>20 and q["impressions"]>100], key=lambda x:x["impressions"], reverse=True)
    if tc:
        print("{:<4} {:<50} {:>7} {:>8} {:>7} {:>7}".format("#","Query","Clicks","Impr","CTR","Pos"))
        print("-"*87)
        for i,q in enumerate(tc[:20],1):
            print("{:<4} {:<50} {:>7,} {:>8,} {:>6.2f}% {:>7.2f}".format(i,q["query"][:48],q["clicks"],q["impressions"],q["ctr"],q["position"]))
        print("  ({} total queries match)".format(len(tc)))
    else:
        print("  No queries match even with relaxed threshold.")
    shdr("2d. All queries containing linkuma")
    lk = sorted([q for q in queries if "linkuma" in q["query"].lower()], key=lambda x:x["impressions"], reverse=True)
    if lk:
        print()
        print("{:<4} {:<50} {:>7} {:>8} {:>7} {:>7}".format("#","Query","Clicks","Impr","CTR","Pos"))
        print("-"*87)
        for i,q in enumerate(lk,1):
            print("{:<4} {:<50} {:>7,} {:>8,} {:>6.2f}% {:>7.2f}".format(i,q["query"][:48],q["clicks"],q["impressions"],q["ctr"],q["position"]))
        tcc=sum(q["clicks"] for q in lk)
        tii=sum(q["impressions"] for q in lk)
        ac=(tcc/tii*100) if tii else 0
        ap=sum(q["position"]*q["impressions"] for q in lk)/tii if tii else 0
        print("-"*87)
        print("     {:<49} {:>7,} {:>8,} {:>6.2f}% {:>7.2f}".format("TOTALS",tcc,tii,ac,ap))
    else:
        print("  No queries containing linkuma found.")

def analyze_pages():
    hdr("3. PAGES.CSV - Page analysis")
    fh = open_csv("Pages")
    reader = csv.DictReader(fh)
    ucol = reader.fieldnames[0]
    pages = []
    for r in reader:
        pages.append({"url":r[ucol],"clicks":pint(r["Clics"]),"impressions":pint(r["Impressions"]),"ctr":pctr(r["CTR"]),"position":pf(r["Position"])})
    fh.close()
    print("  Total pages loaded: {}".format(len(pages)))
    shdr("3a. Duplicate URLs (with/without trailing slash)")
    print("    Split link equity and confuse crawlers. Redirect one to the other.")
    print()
    ug = defaultdict(list)
    for p in pages:
        ug[p["url"].rstrip("/")].append(p)
    dupes = {k:v for k,v in ug.items() if len(v)>1}
    if dupes:
        print("  Found {} URL(s) with trailing-slash duplicates:".format(len(dupes)))
        print()
        for nu,vs in sorted(dupes.items(), key=lambda x:sum(v["impressions"] for v in x[1]), reverse=True):
            tcc=sum(v["clicks"] for v in vs)
            tii=sum(v["impressions"] for v in vs)
            cc=(tcc/tii*100) if tii else 0
            wp=sum(v["position"]*v["impressions"] for v in vs)/tii if tii else 0
            print("  Normalized: {}".format(nu))
            for v in vs:
                tag="(with /)" if v["url"].endswith("/") else "(no /) "
                print("    {}  Clicks: {:>5,}  Impr: {:>7,}  CTR: {:.2f}%  Pos: {:.2f}".format(tag,v["clicks"],v["impressions"],v["ctr"],v["position"]))
            print("    COMBINED  Clicks: {:>5,}  Impr: {:>7,}  CTR: {:.2f}%  Pos: {:.2f}".format(tcc,tii,cc,wp))
            print()
    else:
        print("  No trailing-slash duplicates found.")
    shdr("3b. Low-CTR high-impression pages (CTR < 0.5%) - Top 20 by impressions")
    print("    Visibility but no clicks. Review titles and meta descriptions.")
    print()
    lc = sorted([p for p in pages if p["ctr"]<0.5], key=lambda x:x["impressions"], reverse=True)
    print("{:<4} {:<68} {:>7} {:>8} {:>7} {:>7}".format("#","URL (path)","Clicks","Impr","CTR","Pos"))
    print("-"*105)
    for i,p in enumerate(lc[:20],1):
        sh = p["url"].replace("https://schoolswp.com","")[:66]
        print("{:<4} {:<68} {:>7,} {:>8,} {:>6.2f}% {:>7.2f}".format(i,sh,p["clicks"],p["impressions"],p["ctr"],p["position"]))
    print("  ({} total pages match CTR < 0.5%)".format(len(lc)))
    shdr("3c. English (/en/) pages - possible hreflang issues")
    print("    If EN pages show for FR queries, hreflang may be misconfigured.")
    print()
    ep = sorted([p for p in pages if "/en/" in p["url"].lower()], key=lambda x:x["impressions"], reverse=True)
    if ep:
        print("{:<4} {:<68} {:>7} {:>8} {:>7} {:>7}".format("#","URL (path)","Clicks","Impr","CTR","Pos"))
        print("-"*105)
        for i,p in enumerate(ep,1):
            sh = p["url"].replace("https://schoolswp.com","")[:66]
            print("{:<4} {:<68} {:>7,} {:>8,} {:>6.2f}% {:>7.2f}".format(i,sh,p["clicks"],p["impressions"],p["ctr"],p["position"]))
        tcc=sum(p["clicks"] for p in ep)
        tii=sum(p["impressions"] for p in ep)
        ac=(tcc/tii*100) if tii else 0
        print("-"*105)
        print("     {:<67} {:>7,} {:>8,} {:>6.2f}%".format("TOTALS",tcc,tii,ac))
    else:
        print("  No pages with /en/ prefix found in data.")
        ae = [p for p in pages if any(x in p["url"].lower() for x in ["/en-","-en/","english"])]
        if ae:
            print("  However, found {} pages with other English URL patterns.".format(len(ae)))
            for p in ae[:10]:
                print("    {}  CTR: {:.2f}%  Pos: {:.2f}".format(p["url"][:80],p["ctr"],p["position"]))

if __name__ == "__main__":
    print()
    print("*"*90)
    print("  GOOGLE SEARCH CONSOLE ANALYSIS - schoolswp.com")
    print("  Data: "+BASE)
    print("  Report: "+datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("*"*90)
    analyze_graphique()
    analyze_requetes()
    analyze_pages()
    print()
    print("="*90)
    print("  END OF REPORT")
    print("="*90)
    print()
