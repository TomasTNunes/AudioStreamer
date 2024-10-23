import sponsorblock as sb
client = sb.Client()
segments = client.get_skip_segments("https://www.youtube.com/watch?v=cF1Na4AIecM")
print(segments)