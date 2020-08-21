#import urls
from django_tutorial import urls

def show_urls(urllist, depth=0):
    for entry in urllist:
        print(entry.app_name)
        print(entry.pattern)
        print(entry.url_patterns)

        print(entry.check)
        #print(entry.reverse_dict)
        print("------------------------------------")

        #print("  " * depth, entry.regex.pattern)
        #if hasattr(entry, 'url_patterns'):
        #    show_urls(entry.urlpatterns, depth + 1)

show_urls(urls.urlpatterns)


#['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_app_dict', '_callback_strs', '_check_custom_error_handlers', '_is_callback', '_join_route', '_local', '_namespace_dict', '_populate', '_populated', '_reverse_dict', '_reverse_with_prefix', , 'callback', 'check', 'default_kwargs', 'resolve_error_handler'  ]
