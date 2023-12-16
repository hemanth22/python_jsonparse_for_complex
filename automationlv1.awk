BEGIN {
    print "<html><body>"
    print "<h1>API Live Verification Output</h1>"
}
NR > 0 {
    print "<pre><code class=\"language-xml\">"$0"</code></pre>"
}
END {
    print "<br/>"
    print "</body></html>"
}
