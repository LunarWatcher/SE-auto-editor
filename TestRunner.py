import unittest

from dragon.Post import Post

def mockAnswer(bodyMarkdown):
    return {
        "body_markdown": bodyMarkdown,
        "answer_id": 69621,
        "last_activity_date": 1234321
    }

class TestMarkdownParsing(unittest.TestCase):

    # We only test "everything" for now.
    # In the future, adding edge-cases here may be necessary.
    def testAllTypes(self):
        mPost = """This is a test for a crude markdown "parser" (which is really more of an identifier `than anything else`, but I have a lot of edge-cases to test)

This is plain text.
This is plain text after a newline.

This is plain text after a blank line.
    This is not a code block

    This is a code block

And here's some text

    and another block
Followed by text 

And here's even more text

     ... and (you guessed it)
    another block
```lang-cpp
std::cout << "Followed by backticks" << std::endl;
```
```lang-python
print("Immediately followed by another block")
```
```With an inline triple start```, followed by ``double`` and `single`, and some random **bold**, because why not?

also a [link](https://www.youtube.com/watch?v=dQw4w9WgXcQ) (inline), and another [link][never-gonna-give-you-up] that's named.

![This is not an image](https://www.youtube.com/watch?v=dQw4w9WgXcQ)

[![And neither is this](https://www.youtube.com/watch?v=dQw4w9WgXcQ)](https://www.youtube.com/watch?v=dQw4w9WgXcQ)

... but pretends to be one on a TV show.:tm:



[never-gonna-give-you-up]: https://www.youtube.com/watch?v=dQw4w9WgXcQ"""

        post = Post(mockAnswer(mPost))
        post.unpackBody()
        self.assertEqual(mPost, post.body)


if __name__ == "__main__":
    unittest.main()