def get_page(url, cache):
  if url in cache:
    print(cache[url])
  else:
    cache[url] = "data"
    print("there's no data saved")

def test():
  cache = {
    "/": "Home Page",
    "/about": "About Us Page",
    "/contact": "Contact Us Page"
  }

  get_page("/", cache)
  get_page("/about", cache)
  get_page("/contact", cache)

test()