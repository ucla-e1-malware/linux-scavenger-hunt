from base64 import b64decode

# Please do the lab legitimately - if you need help, just ask us!
exec(b64decode("""aW1wb3J0IG9zCmltcG9ydCBzeXMKaW1wb3J0IHJhbmRvbQppbXBvcnQgaGFzaGxpYgppbXBvcnQgZ2VuZXJhdGVfY2x1ZXMgYXMgZ2MKaW1wb3J0IHN1YnByb2Nlc3MgYXMgc3AKCgpkZWYgc2hlbGxfb3V0KGNvbW0pOgogICAgcmV0dXJuIHNwLnJ1bihjb21tLnNwbGl0KCksIGNhcHR1cmVfb3V0cHV0PVRydWUpLnN0ZG91dC5kZWNvZGUoKQoKCmRlZiBjaGVja19oaW50KGNsdWUsIGhpbnQsIGRpY3Rpb25hcnkpOgogICAgaWYgY2x1ZSA9PSAzOgogICAgICAgIGNvdW50ID0gbGVuKG9zLmxpc3RkaXIoIi91c3IiKSkKICAgICAgICByZXR1cm4gaW50KGhpbnQpID09IGNvdW50CiAgICBlbGlmIGNsdWUgPT0gNDoKICAgICAgICBob3N0bmFtZSA9IG9wZW4oIi9ldGMvaG9zdG5hbWUiLCAiciIpLnJlYWQoKS5zdHJpcCgpCiAgICAgICAgcmV0dXJuIGhpbnQgPT0gaG9zdG5hbWUKICAgIGVsaWYgY2x1ZSA9PSA1OgogICAgICAgIHJldHVybiBoaW50IGluIFsiaSIsICJuIiwgIi1pIiwgIi1uIl0KICAgIGVsaWYgY2x1ZSA9PSA2OgogICAgICAgIHJldHVybiBoaW50ID09IG9zLmdldGVudigiUEFUSCIpLnNwbGl0KCI6IilbMF0KICAgIGVsaWYgY2x1ZSA9PSA3OgogICAgICAgIHJldHVybiBoaW50ID09IHNoZWxsX291dCgid2hpY2ggcHl0aG9uIikuc3RyaXAoKQogICAgZWxpZiBjbHVlID09IDg6CiAgICAgICAgcmV0dXJuIGhpbnQgaW4gWyJhY2NlbCJdCiAgICBlbGlmIGNsdWUgPT0gOToKICAgICAgICB2YWwgPSBzaGVsbF9vdXQoZiJ3YyAtbCB7ZGljdGlvbmFyeX0iKS5zcGxpdCgpWzBdCiAgICAgICAgcmV0dXJuIGhpbnQgPT0gdmFsCiAgICBlbGlmIGNsdWUgPT0gMTA6CiAgICAgICAgcmV0dXJuICgKICAgICAgICAgICAgaGludCA9PSBzaGVsbF9vdXQoZiJncmVwIC1BIDEgdGFjdGZ1bCB7ZGljdGlvbmFyeX0iKS5zdHJpcCgpLnNwbGl0KCJcbiIpWzFdCiAgICAgICAgKQogICAgZWxpZiBjbHVlID09IDExOgogICAgICAgIHdpdGggb3BlbigiUkVBRE1FLm1kIiwgInIiKSBhcyBmOgogICAgICAgICAgICByZXR1cm4gImNhdHMgYXJlIGJldHRlciB0aGFuIGRvZ3MiIGluICIiLmpvaW4oZi5yZWFkbGluZXMoKSkKICAgIGVsaWYgY2x1ZSA9PSAxMjoKICAgICAgICBpZiBub3QgaGludC5zdGFydHN3aXRoKCItIik6CiAgICAgICAgICAgIHJldHVybiBGYWxzZQogICAgICAgIGlmIG5vdCAoImsgNSIgaW4gaGludCBvciAiazUiIGluIGhpbnQpOgogICAgICAgICAgICByZXR1cm4gRmFsc2UKICAgICAgICBpZiBub3QgInIiIGluIGhpbnQ6CiAgICAgICAgICAgIHJldHVybiBGYWxzZQogICAgICAgIGlmIG5vdCAoIm4iIGluIGhpbnQgb3IgImciIGluIGhpbnQpOgogICAgICAgICAgICByZXR1cm4gRmFsc2UKICAgICAgICByZXR1cm4gVHJ1ZQoKCmlmIF9fbmFtZV9fID09ICJfX21haW5fXyI6CgogICAgaWYgbGVuKHN5cy5hcmd2KSAhPSAzOgogICAgICAgIHN5cy5leGl0KCJOZWVkIGEgY2x1ZSBudW1iZXIgYW5kIGhpbnQiKQogICAgY2x1ZV9udW1iZXIgPSBpbnQoc3lzLmFyZ3ZbMV0pCiAgICBoaW50ID0gc3lzLmFyZ3ZbMl0KICAgIHRyeToKICAgICAgICB3aXRoIG9wZW4oIi5zZWNyZXRfbnVtYmVyIiwgInIiKSBhcyBmOgogICAgICAgICAgICBzZWNyZXRfbnVtYmVyID0gaW50KCIiLmpvaW4oZi5yZWFkbGluZXMoKSkpCiAgICBleGNlcHQ6CiAgICAgICAgc3lzLmV4aXQoIkdlbmVyYXRlIHRoZSBjbHVlcyBmaXJzdCEiKQoKICAgIGNsdWVfaW5kZXhlcyA9IGdjLmdlbl9jbHVlX2xpc3QoCiAgICAgICAgZ2MuU1RBUlRfQ0xVRSwgZ2MuTEFTVF9DTFVFLCBnYy5DTFVFX1NQQUNFLCBzZWNyZXRfbnVtYmVyCiAgICApCiAgICBkaWN0aW9uYXJ5ID0gb3BlbigiY29uZiIsICJyIikucmVhZCgpLnN0cmlwKCkKCiAgICBpZiBjaGVja19oaW50KGNsdWVfbnVtYmVyLCBoaW50LCBkaWN0aW9uYXJ5KToKICAgICAgICBwcmludChnYy56ZXJvX3BhZChjbHVlX2luZGV4ZXNbY2x1ZV9udW1iZXIgLSBnYy5TVEFSVF9DTFVFXSkpCiAgICBlbHNlOgogICAgICAgIFIgPSByYW5kb20uUmFuZG9tKCkKICAgICAgICBpZiB0eXBlKGhpbnQpID09IHN0cjoKICAgICAgICAgICAgbWQ1ID0gaGFzaGxpYi5tZDUoaGludC5lbmNvZGUoKSkKICAgICAgICAgICAgaGludF9udW1iZXIgPSBpbnQobWQ1LmhleGRpZ2VzdCgpLCAxNikKICAgICAgICBSLnNlZWQoc2VjcmV0X251bWJlciArIGNsdWVfbnVtYmVyICsgaGludF9udW1iZXIpCiAgICAgICAgcHJpbnQoZ2MuemVyb19wYWQoUi5yYW5kaW50KDEsIGdjLkNMVUVfU1BBQ0UpKSkKCg=="""))
# Please do the lab legitimately - if you need help, just ask us!
