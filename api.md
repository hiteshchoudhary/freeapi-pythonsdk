# Public

## RandomUsers

Types:

```python
from freeapiapp.types.public import RandomUserRetrieveResponse, RandomUserListResponse
```

Methods:

- <code title="get /public/randomusers/{userId}">client.public.random_users.<a href="./src/freeapiapp/resources/public/random_users/random_users.py">retrieve</a>(user_id) -> <a href="./src/freeapiapp/types/public/random_user_retrieve_response.py">RandomUserRetrieveResponse</a></code>
- <code title="get /public/randomusers">client.public.random_users.<a href="./src/freeapiapp/resources/public/random_users/random_users.py">list</a>(\*\*<a href="src/freeapiapp/types/public/random_user_list_params.py">params</a>) -> <a href="./src/freeapiapp/types/public/random_user_list_response.py">RandomUserListResponse</a></code>

### User

Types:

```python
from freeapiapp.types.public.random_users import UserRandomResponse
```

Methods:

- <code title="get /public/randomusers/user/random">client.public.random_users.user.<a href="./src/freeapiapp/resources/public/random_users/user.py">random</a>() -> <a href="./src/freeapiapp/types/public/random_users/user_random_response.py">UserRandomResponse</a></code>

## RandomProducts

Types:

```python
from freeapiapp.types.public import RandomProductRetrieveResponse, RandomProductListResponse
```

Methods:

- <code title="get /public/randomproducts/{productId}">client.public.random_products.<a href="./src/freeapiapp/resources/public/random_products/random_products.py">retrieve</a>(product_id) -> <a href="./src/freeapiapp/types/public/random_product_retrieve_response.py">RandomProductRetrieveResponse</a></code>
- <code title="get /public/randomproducts">client.public.random_products.<a href="./src/freeapiapp/resources/public/random_products/random_products.py">list</a>(\*\*<a href="src/freeapiapp/types/public/random_product_list_params.py">params</a>) -> <a href="./src/freeapiapp/types/public/random_product_list_response.py">RandomProductListResponse</a></code>

### Product

Types:

```python
from freeapiapp.types.public.random_products import ProductRandomResponse
```

Methods:

- <code title="get /public/randomproducts/product/random">client.public.random_products.product.<a href="./src/freeapiapp/resources/public/random_products/product.py">random</a>() -> <a href="./src/freeapiapp/types/public/random_products/product_random_response.py">ProductRandomResponse</a></code>

## RandomJokes

Types:

```python
from freeapiapp.types.public import RandomJokeRetrieveResponse, RandomJokeListResponse
```

Methods:

- <code title="get /public/randomjokes/{jokeId}">client.public.random_jokes.<a href="./src/freeapiapp/resources/public/random_jokes/random_jokes.py">retrieve</a>(joke_id) -> <a href="./src/freeapiapp/types/public/random_joke_retrieve_response.py">RandomJokeRetrieveResponse</a></code>
- <code title="get /public/randomjokes">client.public.random_jokes.<a href="./src/freeapiapp/resources/public/random_jokes/random_jokes.py">list</a>(\*\*<a href="src/freeapiapp/types/public/random_joke_list_params.py">params</a>) -> <a href="./src/freeapiapp/types/public/random_joke_list_response.py">RandomJokeListResponse</a></code>

### Joke

Types:

```python
from freeapiapp.types.public.random_jokes import JokeRandomResponse
```

Methods:

- <code title="get /public/randomjokes/joke/random">client.public.random_jokes.joke.<a href="./src/freeapiapp/resources/public/random_jokes/joke.py">random</a>() -> <a href="./src/freeapiapp/types/public/random_jokes/joke_random_response.py">JokeRandomResponse</a></code>

## Books

Types:

```python
from freeapiapp.types.public import BookRetrieveResponse, BookListResponse, BookRandomResponse
```

Methods:

- <code title="get /public/books/{bookId}">client.public.books.<a href="./src/freeapiapp/resources/public/books.py">retrieve</a>(book_id) -> <a href="./src/freeapiapp/types/public/book_retrieve_response.py">BookRetrieveResponse</a></code>
- <code title="get /public/books">client.public.books.<a href="./src/freeapiapp/resources/public/books.py">list</a>(\*\*<a href="src/freeapiapp/types/public/book_list_params.py">params</a>) -> <a href="./src/freeapiapp/types/public/book_list_response.py">BookListResponse</a></code>
- <code title="get /public/books/book/random">client.public.books.<a href="./src/freeapiapp/resources/public/books.py">random</a>() -> <a href="./src/freeapiapp/types/public/book_random_response.py">BookRandomResponse</a></code>

## Stocks

Types:

```python
from freeapiapp.types.public import StockRetrieveResponse, StockListResponse, StockRandomResponse
```

Methods:

- <code title="get /public/stocks/{stockSymbol}">client.public.stocks.<a href="./src/freeapiapp/resources/public/stocks.py">retrieve</a>(stock_symbol) -> <a href="./src/freeapiapp/types/public/stock_retrieve_response.py">StockRetrieveResponse</a></code>
- <code title="get /public/stocks">client.public.stocks.<a href="./src/freeapiapp/resources/public/stocks.py">list</a>(\*\*<a href="src/freeapiapp/types/public/stock_list_params.py">params</a>) -> <a href="./src/freeapiapp/types/public/stock_list_response.py">StockListResponse</a></code>
- <code title="get /public/stocks/stock/random">client.public.stocks.<a href="./src/freeapiapp/resources/public/stocks.py">random</a>() -> <a href="./src/freeapiapp/types/public/stock_random_response.py">StockRandomResponse</a></code>

## Quotes

Types:

```python
from freeapiapp.types.public import QuoteRetrieveResponse, QuoteListResponse, QuoteRandomResponse
```

Methods:

- <code title="get /public/quotes/{quoteId}">client.public.quotes.<a href="./src/freeapiapp/resources/public/quotes.py">retrieve</a>(quote_id) -> <a href="./src/freeapiapp/types/public/quote_retrieve_response.py">QuoteRetrieveResponse</a></code>
- <code title="get /public/quotes">client.public.quotes.<a href="./src/freeapiapp/resources/public/quotes.py">list</a>(\*\*<a href="src/freeapiapp/types/public/quote_list_params.py">params</a>) -> <a href="./src/freeapiapp/types/public/quote_list_response.py">QuoteListResponse</a></code>
- <code title="get /public/quotes/quote/random">client.public.quotes.<a href="./src/freeapiapp/resources/public/quotes.py">random</a>() -> <a href="./src/freeapiapp/types/public/quote_random_response.py">QuoteRandomResponse</a></code>

## Meals

Types:

```python
from freeapiapp.types.public import MealRetrieveResponse, MealListResponse
```

Methods:

- <code title="get /public/meals/{mealId}">client.public.meals.<a href="./src/freeapiapp/resources/public/meals/meals.py">retrieve</a>(meal_id) -> <a href="./src/freeapiapp/types/public/meal_retrieve_response.py">MealRetrieveResponse</a></code>
- <code title="get /public/meals">client.public.meals.<a href="./src/freeapiapp/resources/public/meals/meals.py">list</a>(\*\*<a href="src/freeapiapp/types/public/meal_list_params.py">params</a>) -> <a href="./src/freeapiapp/types/public/meal_list_response.py">MealListResponse</a></code>

### Meal

Types:

```python
from freeapiapp.types.public.meals import MealRandomResponse
```

Methods:

- <code title="get /public/meals/meal/random">client.public.meals.meal.<a href="./src/freeapiapp/resources/public/meals/meal.py">random</a>() -> <a href="./src/freeapiapp/types/public/meals/meal_random_response.py">MealRandomResponse</a></code>

## Dogs

Types:

```python
from freeapiapp.types.public import DogRetrieveResponse, DogListResponse
```

Methods:

- <code title="get /public/dogs/{dogId}">client.public.dogs.<a href="./src/freeapiapp/resources/public/dogs/dogs.py">retrieve</a>(dog_id) -> <a href="./src/freeapiapp/types/public/dog_retrieve_response.py">DogRetrieveResponse</a></code>
- <code title="get /public/dogs">client.public.dogs.<a href="./src/freeapiapp/resources/public/dogs/dogs.py">list</a>(\*\*<a href="src/freeapiapp/types/public/dog_list_params.py">params</a>) -> <a href="./src/freeapiapp/types/public/dog_list_response.py">DogListResponse</a></code>

### Dog

Types:

```python
from freeapiapp.types.public.dogs import DogRandomResponse
```

Methods:

- <code title="get /public/dogs/dog/random">client.public.dogs.dog.<a href="./src/freeapiapp/resources/public/dogs/dog.py">random</a>() -> <a href="./src/freeapiapp/types/public/dogs/dog_random_response.py">DogRandomResponse</a></code>

## Cats

Types:

```python
from freeapiapp.types.public import CatRetrieveResponse, CatListResponse
```

Methods:

- <code title="get /public/cats/{catId}">client.public.cats.<a href="./src/freeapiapp/resources/public/cats/cats.py">retrieve</a>(cat_id) -> <a href="./src/freeapiapp/types/public/cat_retrieve_response.py">CatRetrieveResponse</a></code>
- <code title="get /public/cats">client.public.cats.<a href="./src/freeapiapp/resources/public/cats/cats.py">list</a>(\*\*<a href="src/freeapiapp/types/public/cat_list_params.py">params</a>) -> <a href="./src/freeapiapp/types/public/cat_list_response.py">CatListResponse</a></code>

### Cat

Types:

```python
from freeapiapp.types.public.cats import CatRandomResponse
```

Methods:

- <code title="get /public/cats/cat/random">client.public.cats.cat.<a href="./src/freeapiapp/resources/public/cats/cat.py">random</a>() -> <a href="./src/freeapiapp/types/public/cats/cat_random_response.py">CatRandomResponse</a></code>

## Youtube

### Channel

Types:

```python
from freeapiapp.types.public.youtube import ChannelListResponse
```

Methods:

- <code title="get /public/youtube/channel">client.public.youtube.channel.<a href="./src/freeapiapp/resources/public/youtube/channel.py">list</a>() -> <a href="./src/freeapiapp/types/public/youtube/channel_list_response.py">ChannelListResponse</a></code>

### Videos

Types:

```python
from freeapiapp.types.public.youtube import VideoRetrieveResponse, VideoListResponse
```

Methods:

- <code title="get /public/youtube/videos/{videoId}">client.public.youtube.videos.<a href="./src/freeapiapp/resources/public/youtube/videos.py">retrieve</a>(video_id) -> <a href="./src/freeapiapp/types/public/youtube/video_retrieve_response.py">VideoRetrieveResponse</a></code>
- <code title="get /public/youtube/videos">client.public.youtube.videos.<a href="./src/freeapiapp/resources/public/youtube/videos.py">list</a>(\*\*<a href="src/freeapiapp/types/public/youtube/video_list_params.py">params</a>) -> <a href="./src/freeapiapp/types/public/youtube/video_list_response.py">VideoListResponse</a></code>

### Comments

Types:

```python
from freeapiapp.types.public.youtube import CommentRetrieveResponse
```

Methods:

- <code title="get /public/youtube/comments/{videoId}">client.public.youtube.comments.<a href="./src/freeapiapp/resources/public/youtube/comments.py">retrieve</a>(video_id) -> <a href="./src/freeapiapp/types/public/youtube/comment_retrieve_response.py">CommentRetrieveResponse</a></code>

### Related

Types:

```python
from freeapiapp.types.public.youtube import RelatedListResponse
```

Methods:

- <code title="get /public/youtube/related/{videoId}">client.public.youtube.related.<a href="./src/freeapiapp/resources/public/youtube/related.py">list</a>(video_id, \*\*<a href="src/freeapiapp/types/public/youtube/related_list_params.py">params</a>) -> <a href="./src/freeapiapp/types/public/youtube/related_list_response.py">RelatedListResponse</a></code>

### Playlists

Types:

```python
from freeapiapp.types.public.youtube import PlaylistRetrieveResponse, PlaylistListResponse
```

Methods:

- <code title="get /public/youtube/playlists/{playlistId}">client.public.youtube.playlists.<a href="./src/freeapiapp/resources/public/youtube/playlists.py">retrieve</a>(playlist_id) -> <a href="./src/freeapiapp/types/public/youtube/playlist_retrieve_response.py">PlaylistRetrieveResponse</a></code>
- <code title="get /public/youtube/playlists">client.public.youtube.playlists.<a href="./src/freeapiapp/resources/public/youtube/playlists.py">list</a>(\*\*<a href="src/freeapiapp/types/public/youtube/playlist_list_params.py">params</a>) -> <a href="./src/freeapiapp/types/public/youtube/playlist_list_response.py">PlaylistListResponse</a></code>

# KitchenSink

## HTTPMethods

Types:

```python
from freeapiapp.types.kitchen_sink import (
    HTTPMethodCreateResponse,
    HTTPMethodUpdateResponse,
    HTTPMethodDeleteResponse,
    HTTPMethodGetResponse,
    HTTPMethodPutResponse,
)
```

Methods:

- <code title="post /kitchen-sink/http-methods/post">client.kitchen_sink.http_methods.<a href="./src/freeapiapp/resources/kitchen_sink/http_methods.py">create</a>() -> <a href="./src/freeapiapp/types/kitchen_sink/http_method_create_response.py">HTTPMethodCreateResponse</a></code>
- <code title="patch /kitchen-sink/http-methods/patch">client.kitchen_sink.http_methods.<a href="./src/freeapiapp/resources/kitchen_sink/http_methods.py">update</a>() -> <a href="./src/freeapiapp/types/kitchen_sink/http_method_update_response.py">HTTPMethodUpdateResponse</a></code>
- <code title="delete /kitchen-sink/http-methods/delete">client.kitchen_sink.http_methods.<a href="./src/freeapiapp/resources/kitchen_sink/http_methods.py">delete</a>() -> <a href="./src/freeapiapp/types/kitchen_sink/http_method_delete_response.py">HTTPMethodDeleteResponse</a></code>
- <code title="get /kitchen-sink/http-methods/get">client.kitchen_sink.http_methods.<a href="./src/freeapiapp/resources/kitchen_sink/http_methods.py">get</a>() -> <a href="./src/freeapiapp/types/kitchen_sink/http_method_get_response.py">HTTPMethodGetResponse</a></code>
- <code title="put /kitchen-sink/http-methods/put">client.kitchen_sink.http_methods.<a href="./src/freeapiapp/resources/kitchen_sink/http_methods.py">put</a>() -> <a href="./src/freeapiapp/types/kitchen_sink/http_method_put_response.py">HTTPMethodPutResponse</a></code>

## StatusCodes

Types:

```python
from freeapiapp.types.kitchen_sink import StatusCodeListResponse
```

Methods:

- <code title="get /kitchen-sink/status-codes/{statusCode}">client.kitchen_sink.status_codes.<a href="./src/freeapiapp/resources/kitchen_sink/status_codes.py">retrieve</a>(status_code) -> None</code>
- <code title="get /kitchen-sink/status-codes">client.kitchen_sink.status_codes.<a href="./src/freeapiapp/resources/kitchen_sink/status_codes.py">list</a>() -> <a href="./src/freeapiapp/types/kitchen_sink/status_code_list_response.py">StatusCodeListResponse</a></code>

## Request

### Headers

Types:

```python
from freeapiapp.types.kitchen_sink.request import HeaderRetrieveResponse
```

Methods:

- <code title="get /kitchen-sink/request/headers">client.kitchen_sink.request.headers.<a href="./src/freeapiapp/resources/kitchen_sink/request/headers.py">retrieve</a>() -> <a href="./src/freeapiapp/types/kitchen_sink/request/header_retrieve_response.py">HeaderRetrieveResponse</a></code>

### IP

Types:

```python
from freeapiapp.types.kitchen_sink.request import IPRetrieveResponse
```

Methods:

- <code title="get /kitchen-sink/request/ip">client.kitchen_sink.request.ip.<a href="./src/freeapiapp/resources/kitchen_sink/request/ip.py">retrieve</a>() -> <a href="./src/freeapiapp/types/kitchen_sink/request/ip_retrieve_response.py">IPRetrieveResponse</a></code>

### UserAgent

Types:

```python
from freeapiapp.types.kitchen_sink.request import UserAgentRetrieveResponse
```

Methods:

- <code title="get /kitchen-sink/request/user-agent">client.kitchen_sink.request.user_agent.<a href="./src/freeapiapp/resources/kitchen_sink/request/user_agent.py">retrieve</a>() -> <a href="./src/freeapiapp/types/kitchen_sink/request/user_agent_retrieve_response.py">UserAgentRetrieveResponse</a></code>

### PathVariable

Types:

```python
from freeapiapp.types.kitchen_sink.request import PathVariableRetrieveResponse
```

Methods:

- <code title="get /kitchen-sink/request/path-variable/{pathVariable}">client.kitchen_sink.request.path_variable.<a href="./src/freeapiapp/resources/kitchen_sink/request/path_variable.py">retrieve</a>(path_variable) -> <a href="./src/freeapiapp/types/kitchen_sink/request/path_variable_retrieve_response.py">PathVariableRetrieveResponse</a></code>

### QueryParameter

Types:

```python
from freeapiapp.types.kitchen_sink.request import QueryParameterRetrieveResponse
```

Methods:

- <code title="get /kitchen-sink/request/query-parameter">client.kitchen_sink.request.query_parameter.<a href="./src/freeapiapp/resources/kitchen_sink/request/query_parameter.py">retrieve</a>(\*\*<a href="src/freeapiapp/types/kitchen_sink/request/query_parameter_retrieve_params.py">params</a>) -> <a href="./src/freeapiapp/types/kitchen_sink/request/query_parameter_retrieve_response.py">QueryParameterRetrieveResponse</a></code>

## Response

### Headers

Types:

```python
from freeapiapp.types.kitchen_sink.response import HeaderRetrieveResponse
```

Methods:

- <code title="get /kitchen-sink/response/headers">client.kitchen_sink.response.headers.<a href="./src/freeapiapp/resources/kitchen_sink/response/headers.py">retrieve</a>() -> <a href="./src/freeapiapp/types/kitchen_sink/response/header_retrieve_response.py">HeaderRetrieveResponse</a></code>

### Cache

Types:

```python
from freeapiapp.types.kitchen_sink.response import CacheRetrieveResponse
```

Methods:

- <code title="get /kitchen-sink/response/cache/{timeToLive}/{cacheResponseDirective}">client.kitchen_sink.response.cache.<a href="./src/freeapiapp/resources/kitchen_sink/response/cache.py">retrieve</a>(cache_response_directive, \*, time_to_live) -> <a href="./src/freeapiapp/types/kitchen_sink/response/cache_retrieve_response.py">CacheRetrieveResponse</a></code>

### HTML

Methods:

- <code title="get /kitchen-sink/response/html">client.kitchen_sink.response.html.<a href="./src/freeapiapp/resources/kitchen_sink/response/html.py">retrieve</a>() -> None</code>

### Xml

Methods:

- <code title="get /kitchen-sink/response/xml">client.kitchen_sink.response.xml.<a href="./src/freeapiapp/resources/kitchen_sink/response/xml.py">retrieve</a>() -> None</code>

# KitchenSinks

Types:

```python
from freeapiapp.types import KitchenSinkResponseBrotliResponse, KitchenSinkResponseGzipResponse
```

Methods:

- <code title="get /kitchen-sink/image/svg">client.kitchen_sinks.<a href="./src/freeapiapp/resources/kitchen_sinks/kitchen_sinks.py">image_svg</a>() -> None</code>
- <code title="get /kitchen-sink/image/jpeg">client.kitchen_sinks.<a href="./src/freeapiapp/resources/kitchen_sinks/kitchen_sinks.py">images_jpeg</a>() -> None</code>
- <code title="get /kitchen-sink/image/jpg">client.kitchen_sinks.<a href="./src/freeapiapp/resources/kitchen_sinks/kitchen_sinks.py">images_jpg</a>() -> None</code>
- <code title="get /kitchen-sink/image/png">client.kitchen_sinks.<a href="./src/freeapiapp/resources/kitchen_sinks/kitchen_sinks.py">images_png</a>() -> None</code>
- <code title="get /kitchen-sink/image/webp">client.kitchen_sinks.<a href="./src/freeapiapp/resources/kitchen_sinks/kitchen_sinks.py">images_webp</a>() -> None</code>
- <code title="get /kitchen-sink/redirect/to">client.kitchen_sinks.<a href="./src/freeapiapp/resources/kitchen_sinks/kitchen_sinks.py">redirect_to</a>(\*\*<a href="src/freeapiapp/types/kitchen_sink_redirect_to_params.py">params</a>) -> None</code>
- <code title="get /kitchen-sink/response/brotli">client.kitchen_sinks.<a href="./src/freeapiapp/resources/kitchen_sinks/kitchen_sinks.py">response_brotli</a>() -> <a href="./src/freeapiapp/types/kitchen_sink_response_brotli_response.py">KitchenSinkResponseBrotliResponse</a></code>
- <code title="get /kitchen-sink/response/gzip">client.kitchen_sinks.<a href="./src/freeapiapp/resources/kitchen_sinks/kitchen_sinks.py">response_gzip</a>() -> <a href="./src/freeapiapp/types/kitchen_sink_response_gzip_response.py">KitchenSinkResponseGzipResponse</a></code>

## Cookies

Types:

```python
from freeapiapp.types.kitchen_sinks import (
    CookieCreateResponse,
    CookieRetrieveResponse,
    CookieRemoveResponse,
)
```

Methods:

- <code title="post /kitchen-sink/cookies/set">client.kitchen_sinks.cookies.<a href="./src/freeapiapp/resources/kitchen_sinks/cookies.py">create</a>(\*\*<a href="src/freeapiapp/types/kitchen_sinks/cookie_create_params.py">params</a>) -> <a href="./src/freeapiapp/types/kitchen_sinks/cookie_create_response.py">CookieCreateResponse</a></code>
- <code title="get /kitchen-sink/cookies/get">client.kitchen_sinks.cookies.<a href="./src/freeapiapp/resources/kitchen_sinks/cookies.py">retrieve</a>() -> <a href="./src/freeapiapp/types/kitchen_sinks/cookie_retrieve_response.py">CookieRetrieveResponse</a></code>
- <code title="delete /kitchen-sink/cookies/remove">client.kitchen_sinks.cookies.<a href="./src/freeapiapp/resources/kitchen_sinks/cookies.py">remove</a>(\*\*<a href="src/freeapiapp/types/kitchen_sinks/cookie_remove_params.py">params</a>) -> <a href="./src/freeapiapp/types/kitchen_sinks/cookie_remove_response.py">CookieRemoveResponse</a></code>

# Authentications

Types:

```python
from freeapiapp.types import (
    AuthenticationCurrentUserResponse,
    AuthenticationLoginResponse,
    AuthenticationLogoutResponse,
    AuthenticationRegisterResponse,
    AuthenticationVerifyEmailResponse,
)
```

Methods:

- <code title="get /users/current-user">client.authentications.<a href="./src/freeapiapp/resources/authentications.py">current_user</a>() -> <a href="./src/freeapiapp/types/authentication_current_user_response.py">AuthenticationCurrentUserResponse</a></code>
- <code title="get /users/github/callback">client.authentications.<a href="./src/freeapiapp/resources/authentications.py">github_callback</a>() -> None</code>
- <code title="get /users/github">client.authentications.<a href="./src/freeapiapp/resources/authentications.py">github_redirect</a>() -> None</code>
- <code title="get /users/google/callback">client.authentications.<a href="./src/freeapiapp/resources/authentications.py">google_callback</a>() -> None</code>
- <code title="get /users/google">client.authentications.<a href="./src/freeapiapp/resources/authentications.py">google_redirect</a>() -> None</code>
- <code title="post /users/login">client.authentications.<a href="./src/freeapiapp/resources/authentications.py">login</a>(\*\*<a href="src/freeapiapp/types/authentication_login_params.py">params</a>) -> <a href="./src/freeapiapp/types/authentication_login_response.py">AuthenticationLoginResponse</a></code>
- <code title="post /users/logout">client.authentications.<a href="./src/freeapiapp/resources/authentications.py">logout</a>() -> <a href="./src/freeapiapp/types/authentication_logout_response.py">AuthenticationLogoutResponse</a></code>
- <code title="post /users/register">client.authentications.<a href="./src/freeapiapp/resources/authentications.py">register</a>(\*\*<a href="src/freeapiapp/types/authentication_register_params.py">params</a>) -> <a href="./src/freeapiapp/types/authentication_register_response.py">AuthenticationRegisterResponse</a></code>
- <code title="get /users/verify-email/{verificationToken}">client.authentications.<a href="./src/freeapiapp/resources/authentications.py">verify_email</a>(verification_token) -> <a href="./src/freeapiapp/types/authentication_verify_email_response.py">AuthenticationVerifyEmailResponse</a></code>

# Users

Types:

```python
from freeapiapp.types import (
    UserAssignRoleResponse,
    UserChangePasswordResponse,
    UserForgotPasswordResponse,
    UserRefreshTokenResponse,
    UserResendEmailVerificationResponse,
    UserResetPasswordResponse,
)
```

Methods:

- <code title="post /users/assign-role/{userId}">client.users.<a href="./src/freeapiapp/resources/users/users.py">assign_role</a>(user_id, \*\*<a href="src/freeapiapp/types/user_assign_role_params.py">params</a>) -> <a href="./src/freeapiapp/types/user_assign_role_response.py">UserAssignRoleResponse</a></code>
- <code title="post /users/change-password">client.users.<a href="./src/freeapiapp/resources/users/users.py">change_password</a>(\*\*<a href="src/freeapiapp/types/user_change_password_params.py">params</a>) -> <a href="./src/freeapiapp/types/user_change_password_response.py">UserChangePasswordResponse</a></code>
- <code title="post /users/forgot-password">client.users.<a href="./src/freeapiapp/resources/users/users.py">forgot_password</a>(\*\*<a href="src/freeapiapp/types/user_forgot_password_params.py">params</a>) -> <a href="./src/freeapiapp/types/user_forgot_password_response.py">UserForgotPasswordResponse</a></code>
- <code title="post /users/refresh-token">client.users.<a href="./src/freeapiapp/resources/users/users.py">refresh_token</a>() -> <a href="./src/freeapiapp/types/user_refresh_token_response.py">UserRefreshTokenResponse</a></code>
- <code title="post /users/resend-email-verification">client.users.<a href="./src/freeapiapp/resources/users/users.py">resend_email_verification</a>() -> <a href="./src/freeapiapp/types/user_resend_email_verification_response.py">UserResendEmailVerificationResponse</a></code>
- <code title="post /users/reset-password/{resetToken}">client.users.<a href="./src/freeapiapp/resources/users/users.py">reset_password</a>(reset_token, \*\*<a href="src/freeapiapp/types/user_reset_password_params.py">params</a>) -> <a href="./src/freeapiapp/types/user_reset_password_response.py">UserResetPasswordResponse</a></code>

## Avatar

Types:

```python
from freeapiapp.types.users import AvatarUpdateResponse
```

Methods:

- <code title="patch /users/avatar">client.users.avatar.<a href="./src/freeapiapp/resources/users/avatar.py">update</a>(\*\*<a href="src/freeapiapp/types/users/avatar_update_params.py">params</a>) -> <a href="./src/freeapiapp/types/users/avatar_update_response.py">AvatarUpdateResponse</a></code>

# Ecommerce

## Profile

Types:

```python
from freeapiapp.types.ecommerce import ProfileRetrieveResponse, ProfileUpdateResponse
```

Methods:

- <code title="get /ecommerce/profile">client.ecommerce.profile.<a href="./src/freeapiapp/resources/ecommerce/profile/profile.py">retrieve</a>() -> <a href="./src/freeapiapp/types/ecommerce/profile_retrieve_response.py">ProfileRetrieveResponse</a></code>
- <code title="patch /ecommerce/profile">client.ecommerce.profile.<a href="./src/freeapiapp/resources/ecommerce/profile/profile.py">update</a>(\*\*<a href="src/freeapiapp/types/ecommerce/profile_update_params.py">params</a>) -> <a href="./src/freeapiapp/types/ecommerce/profile_update_response.py">ProfileUpdateResponse</a></code>

### MyOrders

Types:

```python
from freeapiapp.types.ecommerce.profile import MyOrderListResponse
```

Methods:

- <code title="get /ecommerce/profile/my-orders">client.ecommerce.profile.my_orders.<a href="./src/freeapiapp/resources/ecommerce/profile/my_orders.py">list</a>(\*\*<a href="src/freeapiapp/types/ecommerce/profile/my_order_list_params.py">params</a>) -> <a href="./src/freeapiapp/types/ecommerce/profile/my_order_list_response.py">MyOrderListResponse</a></code>

## Cart

Types:

```python
from freeapiapp.types.ecommerce import CartClearResponse
```

Methods:

- <code title="delete /ecommerce/cart/clear">client.ecommerce.cart.<a href="./src/freeapiapp/resources/ecommerce/cart.py">clear</a>() -> <a href="./src/freeapiapp/types/ecommerce/cart_clear_response.py">CartClearResponse</a></code>

## Categories

Types:

```python
from freeapiapp.types.ecommerce import (
    CategoryCreateResponse,
    CategoryRetrieveResponse,
    CategoryUpdateResponse,
    CategoryListResponse,
    CategoryDeleteResponse,
)
```

Methods:

- <code title="post /ecommerce/categories">client.ecommerce.categories.<a href="./src/freeapiapp/resources/ecommerce/categories.py">create</a>(\*\*<a href="src/freeapiapp/types/ecommerce/category_create_params.py">params</a>) -> <a href="./src/freeapiapp/types/ecommerce/category_create_response.py">CategoryCreateResponse</a></code>
- <code title="get /ecommerce/categories/{categoryId}">client.ecommerce.categories.<a href="./src/freeapiapp/resources/ecommerce/categories.py">retrieve</a>(category_id) -> <a href="./src/freeapiapp/types/ecommerce/category_retrieve_response.py">CategoryRetrieveResponse</a></code>
- <code title="patch /ecommerce/categories/{categoryId}">client.ecommerce.categories.<a href="./src/freeapiapp/resources/ecommerce/categories.py">update</a>(category_id, \*\*<a href="src/freeapiapp/types/ecommerce/category_update_params.py">params</a>) -> <a href="./src/freeapiapp/types/ecommerce/category_update_response.py">CategoryUpdateResponse</a></code>
- <code title="get /ecommerce/categories">client.ecommerce.categories.<a href="./src/freeapiapp/resources/ecommerce/categories.py">list</a>(\*\*<a href="src/freeapiapp/types/ecommerce/category_list_params.py">params</a>) -> <a href="./src/freeapiapp/types/ecommerce/category_list_response.py">CategoryListResponse</a></code>
- <code title="delete /ecommerce/categories/{categoryId}">client.ecommerce.categories.<a href="./src/freeapiapp/resources/ecommerce/categories.py">delete</a>(category_id) -> <a href="./src/freeapiapp/types/ecommerce/category_delete_response.py">CategoryDeleteResponse</a></code>

## Coupons

Types:

```python
from freeapiapp.types.ecommerce import (
    CouponCreateResponse,
    CouponRetrieveResponse,
    CouponUpdateResponse,
    CouponListResponse,
    CouponDeleteResponse,
    CouponApplyResponse,
    CouponRemoveResponse,
)
```

Methods:

- <code title="post /ecommerce/coupons">client.ecommerce.coupons.<a href="./src/freeapiapp/resources/ecommerce/coupons/coupons.py">create</a>(\*\*<a href="src/freeapiapp/types/ecommerce/coupon_create_params.py">params</a>) -> <a href="./src/freeapiapp/types/ecommerce/coupon_create_response.py">CouponCreateResponse</a></code>
- <code title="get /ecommerce/coupons/{couponId}">client.ecommerce.coupons.<a href="./src/freeapiapp/resources/ecommerce/coupons/coupons.py">retrieve</a>(coupon_id) -> <a href="./src/freeapiapp/types/ecommerce/coupon_retrieve_response.py">CouponRetrieveResponse</a></code>
- <code title="patch /ecommerce/coupons/{couponId}">client.ecommerce.coupons.<a href="./src/freeapiapp/resources/ecommerce/coupons/coupons.py">update</a>(coupon_id, \*\*<a href="src/freeapiapp/types/ecommerce/coupon_update_params.py">params</a>) -> <a href="./src/freeapiapp/types/ecommerce/coupon_update_response.py">CouponUpdateResponse</a></code>
- <code title="get /ecommerce/coupons">client.ecommerce.coupons.<a href="./src/freeapiapp/resources/ecommerce/coupons/coupons.py">list</a>(\*\*<a href="src/freeapiapp/types/ecommerce/coupon_list_params.py">params</a>) -> <a href="./src/freeapiapp/types/ecommerce/coupon_list_response.py">CouponListResponse</a></code>
- <code title="delete /ecommerce/coupons/{couponId}">client.ecommerce.coupons.<a href="./src/freeapiapp/resources/ecommerce/coupons/coupons.py">delete</a>(coupon_id) -> <a href="./src/freeapiapp/types/ecommerce/coupon_delete_response.py">CouponDeleteResponse</a></code>
- <code title="post /ecommerce/coupons/c/apply">client.ecommerce.coupons.<a href="./src/freeapiapp/resources/ecommerce/coupons/coupons.py">apply</a>(\*\*<a href="src/freeapiapp/types/ecommerce/coupon_apply_params.py">params</a>) -> <a href="./src/freeapiapp/types/ecommerce/coupon_apply_response.py">CouponApplyResponse</a></code>
- <code title="post /ecommerce/coupons/c/remove">client.ecommerce.coupons.<a href="./src/freeapiapp/resources/ecommerce/coupons/coupons.py">remove</a>(\*\*<a href="src/freeapiapp/types/ecommerce/coupon_remove_params.py">params</a>) -> <a href="./src/freeapiapp/types/ecommerce/coupon_remove_response.py">CouponRemoveResponse</a></code>

### CustomerAvailable

Types:

```python
from freeapiapp.types.ecommerce.coupons import CustomerAvailableListResponse
```

Methods:

- <code title="get /ecommerce/coupons/customer/available">client.ecommerce.coupons.customer_available.<a href="./src/freeapiapp/resources/ecommerce/coupons/customer_available.py">list</a>(\*\*<a href="src/freeapiapp/types/ecommerce/coupons/customer_available_list_params.py">params</a>) -> <a href="./src/freeapiapp/types/ecommerce/coupons/customer_available_list_response.py">CustomerAvailableListResponse</a></code>

### Status

Types:

```python
from freeapiapp.types.ecommerce.coupons import StatusUpdateResponse
```

Methods:

- <code title="patch /ecommerce/coupons/status/{couponId}">client.ecommerce.coupons.status.<a href="./src/freeapiapp/resources/ecommerce/coupons/status.py">update</a>(coupon_id, \*\*<a href="src/freeapiapp/types/ecommerce/coupons/status_update_params.py">params</a>) -> <a href="./src/freeapiapp/types/ecommerce/coupons/status_update_response.py">StatusUpdateResponse</a></code>

## Addresses

Types:

```python
from freeapiapp.types.ecommerce import (
    AddressCreateResponse,
    AddressRetrieveResponse,
    AddressUpdateResponse,
    AddressListResponse,
    AddressDeleteResponse,
)
```

Methods:

- <code title="post /ecommerce/addresses">client.ecommerce.addresses.<a href="./src/freeapiapp/resources/ecommerce/addresses.py">create</a>(\*\*<a href="src/freeapiapp/types/ecommerce/address_create_params.py">params</a>) -> <a href="./src/freeapiapp/types/ecommerce/address_create_response.py">AddressCreateResponse</a></code>
- <code title="get /ecommerce/addresses/{addressId}">client.ecommerce.addresses.<a href="./src/freeapiapp/resources/ecommerce/addresses.py">retrieve</a>(address_id) -> <a href="./src/freeapiapp/types/ecommerce/address_retrieve_response.py">AddressRetrieveResponse</a></code>
- <code title="patch /ecommerce/addresses/{addressId}">client.ecommerce.addresses.<a href="./src/freeapiapp/resources/ecommerce/addresses.py">update</a>(address_id, \*\*<a href="src/freeapiapp/types/ecommerce/address_update_params.py">params</a>) -> <a href="./src/freeapiapp/types/ecommerce/address_update_response.py">AddressUpdateResponse</a></code>
- <code title="get /ecommerce/addresses">client.ecommerce.addresses.<a href="./src/freeapiapp/resources/ecommerce/addresses.py">list</a>(\*\*<a href="src/freeapiapp/types/ecommerce/address_list_params.py">params</a>) -> <a href="./src/freeapiapp/types/ecommerce/address_list_response.py">AddressListResponse</a></code>
- <code title="delete /ecommerce/addresses/{addressId}">client.ecommerce.addresses.<a href="./src/freeapiapp/resources/ecommerce/addresses.py">delete</a>(address_id) -> <a href="./src/freeapiapp/types/ecommerce/address_delete_response.py">AddressDeleteResponse</a></code>

## Orders

Types:

```python
from freeapiapp.types.ecommerce import OrderRetrieveResponse
```

Methods:

- <code title="get /ecommerce/orders/{orderId}">client.ecommerce.orders.<a href="./src/freeapiapp/resources/ecommerce/orders/orders.py">retrieve</a>(order_id) -> <a href="./src/freeapiapp/types/ecommerce/order_retrieve_response.py">OrderRetrieveResponse</a></code>

### Admin

Types:

```python
from freeapiapp.types.ecommerce.orders import AdminListResponse
```

Methods:

- <code title="get /ecommerce/orders/list/admin">client.ecommerce.orders.admin.<a href="./src/freeapiapp/resources/ecommerce/orders/admin.py">list</a>(\*\*<a href="src/freeapiapp/types/ecommerce/orders/admin_list_params.py">params</a>) -> <a href="./src/freeapiapp/types/ecommerce/orders/admin_list_response.py">AdminListResponse</a></code>

### Provider

#### Razorpay

Types:

```python
from freeapiapp.types.ecommerce.orders.provider import (
    RazorpayCreateResponse,
    RazorpayVerifyPaymentResponse,
)
```

Methods:

- <code title="post /ecommerce/orders/provider/razorpay">client.ecommerce.orders.provider.razorpay.<a href="./src/freeapiapp/resources/ecommerce/orders/provider/razorpay.py">create</a>(\*\*<a href="src/freeapiapp/types/ecommerce/orders/provider/razorpay_create_params.py">params</a>) -> <a href="./src/freeapiapp/types/ecommerce/orders/provider/razorpay_create_response.py">RazorpayCreateResponse</a></code>
- <code title="post /ecommerce/orders/provider/razorpay/verify-payment">client.ecommerce.orders.provider.razorpay.<a href="./src/freeapiapp/resources/ecommerce/orders/provider/razorpay.py">verify_payment</a>(\*\*<a href="src/freeapiapp/types/ecommerce/orders/provider/razorpay_verify_payment_params.py">params</a>) -> <a href="./src/freeapiapp/types/ecommerce/orders/provider/razorpay_verify_payment_response.py">RazorpayVerifyPaymentResponse</a></code>

#### Paypal

Types:

```python
from freeapiapp.types.ecommerce.orders.provider import PaypalCreateResponse
```

Methods:

- <code title="post /ecommerce/orders/provider/paypal">client.ecommerce.orders.provider.paypal.<a href="./src/freeapiapp/resources/ecommerce/orders/provider/paypal.py">create</a>(\*\*<a href="src/freeapiapp/types/ecommerce/orders/provider/paypal_create_params.py">params</a>) -> <a href="./src/freeapiapp/types/ecommerce/orders/provider/paypal_create_response.py">PaypalCreateResponse</a></code>
- <code title="post /ecommerce/orders/provider/paypal/verify-payment">client.ecommerce.orders.provider.paypal.<a href="./src/freeapiapp/resources/ecommerce/orders/provider/paypal.py">verify_payment</a>(\*\*<a href="src/freeapiapp/types/ecommerce/orders/provider/paypal_verify_payment_params.py">params</a>) -> None</code>

### Status

Types:

```python
from freeapiapp.types.ecommerce.orders import StatusUpdateResponse
```

Methods:

- <code title="patch /ecommerce/orders/status/{orderId}">client.ecommerce.orders.status.<a href="./src/freeapiapp/resources/ecommerce/orders/status.py">update</a>(order_id, \*\*<a href="src/freeapiapp/types/ecommerce/orders/status_update_params.py">params</a>) -> <a href="./src/freeapiapp/types/ecommerce/orders/status_update_response.py">StatusUpdateResponse</a></code>

# Products

Types:

```python
from freeapiapp.types import (
    ProductCreateResponse,
    ProductRetrieveResponse,
    ProductUpdateResponse,
    ProductListResponse,
    ProductDeleteResponse,
)
```

Methods:

- <code title="post /ecommerce/products">client.products.<a href="./src/freeapiapp/resources/products/products.py">create</a>(\*\*<a href="src/freeapiapp/types/product_create_params.py">params</a>) -> <a href="./src/freeapiapp/types/product_create_response.py">ProductCreateResponse</a></code>
- <code title="get /ecommerce/products/{productId}">client.products.<a href="./src/freeapiapp/resources/products/products.py">retrieve</a>(product_id) -> <a href="./src/freeapiapp/types/product_retrieve_response.py">ProductRetrieveResponse</a></code>
- <code title="patch /ecommerce/products/{productId}">client.products.<a href="./src/freeapiapp/resources/products/products.py">update</a>(product_id, \*\*<a href="src/freeapiapp/types/product_update_params.py">params</a>) -> <a href="./src/freeapiapp/types/product_update_response.py">ProductUpdateResponse</a></code>
- <code title="get /ecommerce/products">client.products.<a href="./src/freeapiapp/resources/products/products.py">list</a>(\*\*<a href="src/freeapiapp/types/product_list_params.py">params</a>) -> <a href="./src/freeapiapp/types/product_list_response.py">ProductListResponse</a></code>
- <code title="delete /ecommerce/products/{productId}">client.products.<a href="./src/freeapiapp/resources/products/products.py">delete</a>(product_id) -> <a href="./src/freeapiapp/types/product_delete_response.py">ProductDeleteResponse</a></code>

## Category

Types:

```python
from freeapiapp.types.products import CategoryRetrieveResponse
```

Methods:

- <code title="get /ecommerce/products/category/{categoryId}">client.products.category.<a href="./src/freeapiapp/resources/products/category.py">retrieve</a>(category_id, \*\*<a href="src/freeapiapp/types/products/category_retrieve_params.py">params</a>) -> <a href="./src/freeapiapp/types/products/category_retrieve_response.py">CategoryRetrieveResponse</a></code>

## Subimage

Types:

```python
from freeapiapp.types.products import SubimageRemoveResponse
```

Methods:

- <code title="patch /ecommerce/products/remove/subimage/{productId}/{subImageId}">client.products.subimage.<a href="./src/freeapiapp/resources/products/subimage.py">remove</a>(sub_image_id, \*, product_id) -> <a href="./src/freeapiapp/types/products/subimage_remove_response.py">SubimageRemoveResponse</a></code>

# Cart

Types:

```python
from freeapiapp.types import CartRetrieveResponse
```

Methods:

- <code title="get /ecommerce/cart">client.cart.<a href="./src/freeapiapp/resources/cart/cart.py">retrieve</a>() -> <a href="./src/freeapiapp/types/cart_retrieve_response.py">CartRetrieveResponse</a></code>

## Item

Types:

```python
from freeapiapp.types.cart import ItemCreateResponse, ItemDeleteResponse
```

Methods:

- <code title="post /ecommerce/cart/item/{productId}">client.cart.item.<a href="./src/freeapiapp/resources/cart/item.py">create</a>(product_id, \*\*<a href="src/freeapiapp/types/cart/item_create_params.py">params</a>) -> <a href="./src/freeapiapp/types/cart/item_create_response.py">ItemCreateResponse</a></code>
- <code title="delete /ecommerce/cart/item/{productId}">client.cart.item.<a href="./src/freeapiapp/resources/cart/item.py">delete</a>(product_id) -> <a href="./src/freeapiapp/types/cart/item_delete_response.py">ItemDeleteResponse</a></code>

# Todos

Types:

```python
from freeapiapp.types import (
    TodoCreateResponse,
    TodoRetrieveResponse,
    TodoUpdateResponse,
    TodoListResponse,
    TodoDeleteResponse,
    TodoToggleStatusResponse,
)
```

Methods:

- <code title="post /todos/">client.todos.<a href="./src/freeapiapp/resources/todos.py">create</a>(\*\*<a href="src/freeapiapp/types/todo_create_params.py">params</a>) -> <a href="./src/freeapiapp/types/todo_create_response.py">TodoCreateResponse</a></code>
- <code title="get /todos/{todoId}">client.todos.<a href="./src/freeapiapp/resources/todos.py">retrieve</a>(todo_id) -> <a href="./src/freeapiapp/types/todo_retrieve_response.py">TodoRetrieveResponse</a></code>
- <code title="patch /todos/{todoId}">client.todos.<a href="./src/freeapiapp/resources/todos.py">update</a>(todo_id, \*\*<a href="src/freeapiapp/types/todo_update_params.py">params</a>) -> <a href="./src/freeapiapp/types/todo_update_response.py">TodoUpdateResponse</a></code>
- <code title="get /todos">client.todos.<a href="./src/freeapiapp/resources/todos.py">list</a>(\*\*<a href="src/freeapiapp/types/todo_list_params.py">params</a>) -> <a href="./src/freeapiapp/types/todo_list_response.py">TodoListResponse</a></code>
- <code title="delete /todos/{todoId}">client.todos.<a href="./src/freeapiapp/resources/todos.py">delete</a>(todo_id) -> <a href="./src/freeapiapp/types/todo_delete_response.py">TodoDeleteResponse</a></code>
- <code title="patch /todos/toggle/status/{todoId}">client.todos.<a href="./src/freeapiapp/resources/todos.py">toggle_status</a>(todo_id) -> <a href="./src/freeapiapp/types/todo_toggle_status_response.py">TodoToggleStatusResponse</a></code>

# SocialMedia

## Profile

Types:

```python
from freeapiapp.types.social_media import ProfileRetrieveResponse, ProfileUpdateResponse
```

Methods:

- <code title="get /social-media/profile/u/{username}">client.social_media.profile.<a href="./src/freeapiapp/resources/social_media/profile/profile.py">retrieve</a>(username) -> <a href="./src/freeapiapp/types/social_media/profile_retrieve_response.py">ProfileRetrieveResponse</a></code>
- <code title="patch /social-media/profile">client.social_media.profile.<a href="./src/freeapiapp/resources/social_media/profile/profile.py">update</a>(\*\*<a href="src/freeapiapp/types/social_media/profile_update_params.py">params</a>) -> <a href="./src/freeapiapp/types/social_media/profile_update_response.py">ProfileUpdateResponse</a></code>

### CoverImage

Types:

```python
from freeapiapp.types.social_media.profile import CoverImageUpdateResponse
```

Methods:

- <code title="patch /social-media/profile/cover-image">client.social_media.profile.cover_image.<a href="./src/freeapiapp/resources/social_media/profile/cover_image.py">update</a>(\*\*<a href="src/freeapiapp/types/social_media/profile/cover_image_update_params.py">params</a>) -> <a href="./src/freeapiapp/types/social_media/profile/cover_image_update_response.py">CoverImageUpdateResponse</a></code>

## Posts

Types:

```python
from freeapiapp.types.social_media import (
    PostCreateResponse,
    PostRetrieveResponse,
    PostUpdateResponse,
    PostListResponse,
    PostDeleteResponse,
    PostLikeResponse,
)
```

Methods:

- <code title="post /social-media/posts">client.social_media.posts.<a href="./src/freeapiapp/resources/social_media/posts/posts.py">create</a>(\*\*<a href="src/freeapiapp/types/social_media/post_create_params.py">params</a>) -> <a href="./src/freeapiapp/types/social_media/post_create_response.py">PostCreateResponse</a></code>
- <code title="get /social-media/posts/{postId}">client.social_media.posts.<a href="./src/freeapiapp/resources/social_media/posts/posts.py">retrieve</a>(post_id) -> <a href="./src/freeapiapp/types/social_media/post_retrieve_response.py">PostRetrieveResponse</a></code>
- <code title="patch /social-media/posts/{postId}">client.social_media.posts.<a href="./src/freeapiapp/resources/social_media/posts/posts.py">update</a>(post_id, \*\*<a href="src/freeapiapp/types/social_media/post_update_params.py">params</a>) -> <a href="./src/freeapiapp/types/social_media/post_update_response.py">PostUpdateResponse</a></code>
- <code title="get /social-media/posts">client.social_media.posts.<a href="./src/freeapiapp/resources/social_media/posts/posts.py">list</a>(\*\*<a href="src/freeapiapp/types/social_media/post_list_params.py">params</a>) -> <a href="./src/freeapiapp/types/social_media/post_list_response.py">PostListResponse</a></code>
- <code title="delete /social-media/posts/{postId}">client.social_media.posts.<a href="./src/freeapiapp/resources/social_media/posts/posts.py">delete</a>(post_id) -> <a href="./src/freeapiapp/types/social_media/post_delete_response.py">PostDeleteResponse</a></code>
- <code title="post /social-media/like/post/{postId}">client.social_media.posts.<a href="./src/freeapiapp/resources/social_media/posts/posts.py">like</a>(post_id) -> <a href="./src/freeapiapp/types/social_media/post_like_response.py">PostLikeResponse</a></code>

### My

Types:

```python
from freeapiapp.types.social_media.posts import MyListResponse
```

Methods:

- <code title="get /social-media/posts/get/my">client.social_media.posts.my.<a href="./src/freeapiapp/resources/social_media/posts/my.py">list</a>(\*\*<a href="src/freeapiapp/types/social_media/posts/my_list_params.py">params</a>) -> <a href="./src/freeapiapp/types/social_media/posts/my_list_response.py">MyListResponse</a></code>

### UserPosts

Types:

```python
from freeapiapp.types.social_media.posts import UserPostListResponse
```

Methods:

- <code title="get /social-media/posts/get/u/{username}">client.social_media.posts.user_posts.<a href="./src/freeapiapp/resources/social_media/posts/user_posts.py">list</a>(username, \*\*<a href="src/freeapiapp/types/social_media/posts/user_post_list_params.py">params</a>) -> <a href="./src/freeapiapp/types/social_media/posts/user_post_list_response.py">UserPostListResponse</a></code>

### Tag

Types:

```python
from freeapiapp.types.social_media.posts import TagListResponse
```

Methods:

- <code title="get /social-media/posts/get/t/{tag}">client.social_media.posts.tag.<a href="./src/freeapiapp/resources/social_media/posts/tag.py">list</a>(tag, \*\*<a href="src/freeapiapp/types/social_media/posts/tag_list_params.py">params</a>) -> <a href="./src/freeapiapp/types/social_media/posts/tag_list_response.py">TagListResponse</a></code>

### Images

Types:

```python
from freeapiapp.types.social_media.posts import ImageRemoveResponse
```

Methods:

- <code title="patch /social-media/posts/remove/image/{postId}/{imageId}">client.social_media.posts.images.<a href="./src/freeapiapp/resources/social_media/posts/images.py">remove</a>(image_id, \*, post_id) -> <a href="./src/freeapiapp/types/social_media/posts/image_remove_response.py">ImageRemoveResponse</a></code>

## Comments

Types:

```python
from freeapiapp.types.social_media import (
    CommentCreateResponse,
    CommentUpdateResponse,
    CommentListResponse,
    CommentDeleteResponse,
    CommentLikeResponse,
)
```

Methods:

- <code title="post /social-media/comments/post/{postId}">client.social_media.comments.<a href="./src/freeapiapp/resources/social_media/comments.py">create</a>(post_id, \*\*<a href="src/freeapiapp/types/social_media/comment_create_params.py">params</a>) -> <a href="./src/freeapiapp/types/social_media/comment_create_response.py">CommentCreateResponse</a></code>
- <code title="patch /social-media/comments/{commentId}">client.social_media.comments.<a href="./src/freeapiapp/resources/social_media/comments.py">update</a>(comment_id, \*\*<a href="src/freeapiapp/types/social_media/comment_update_params.py">params</a>) -> <a href="./src/freeapiapp/types/social_media/comment_update_response.py">CommentUpdateResponse</a></code>
- <code title="get /social-media/comments/post/{postId}">client.social_media.comments.<a href="./src/freeapiapp/resources/social_media/comments.py">list</a>(post_id, \*\*<a href="src/freeapiapp/types/social_media/comment_list_params.py">params</a>) -> <a href="./src/freeapiapp/types/social_media/comment_list_response.py">CommentListResponse</a></code>
- <code title="delete /social-media/comments/{commentId}">client.social_media.comments.<a href="./src/freeapiapp/resources/social_media/comments.py">delete</a>(comment_id) -> <a href="./src/freeapiapp/types/social_media/comment_delete_response.py">CommentDeleteResponse</a></code>
- <code title="post /social-media/like/comment/{commentId}">client.social_media.comments.<a href="./src/freeapiapp/resources/social_media/comments.py">like</a>(comment_id) -> <a href="./src/freeapiapp/types/social_media/comment_like_response.py">CommentLikeResponse</a></code>

## Bookmarks

Types:

```python
from freeapiapp.types.social_media import BookmarkCreateResponse, BookmarkRetrieveResponse
```

Methods:

- <code title="post /social-media/bookmarks/{postId}">client.social_media.bookmarks.<a href="./src/freeapiapp/resources/social_media/bookmarks.py">create</a>(post_id) -> <a href="./src/freeapiapp/types/social_media/bookmark_create_response.py">BookmarkCreateResponse</a></code>
- <code title="get /social-media/bookmarks">client.social_media.bookmarks.<a href="./src/freeapiapp/resources/social_media/bookmarks.py">retrieve</a>(\*\*<a href="src/freeapiapp/types/social_media/bookmark_retrieve_params.py">params</a>) -> <a href="./src/freeapiapp/types/social_media/bookmark_retrieve_response.py">BookmarkRetrieveResponse</a></code>

## Follow

### Followers

Types:

```python
from freeapiapp.types.social_media.follow import FollowerListResponse
```

Methods:

- <code title="get /social-media/follow/list/followers/{username}">client.social_media.follow.followers.<a href="./src/freeapiapp/resources/social_media/follow/followers.py">list</a>(username, \*\*<a href="src/freeapiapp/types/social_media/follow/follower_list_params.py">params</a>) -> <a href="./src/freeapiapp/types/social_media/follow/follower_list_response.py">FollowerListResponse</a></code>

### Following

Types:

```python
from freeapiapp.types.social_media.follow import FollowingListResponse
```

Methods:

- <code title="get /social-media/follow/list/following/{username}">client.social_media.follow.following.<a href="./src/freeapiapp/resources/social_media/follow/following.py">list</a>(username, \*\*<a href="src/freeapiapp/types/social_media/follow/following_list_params.py">params</a>) -> <a href="./src/freeapiapp/types/social_media/follow/following_list_response.py">FollowingListResponse</a></code>

# ChatApp

## Chats

Types:

```python
from freeapiapp.types.chat_app import ChatListResponse
```

Methods:

- <code title="get /chat-app/chats">client.chat_app.chats.<a href="./src/freeapiapp/resources/chat_app/chats/chats.py">list</a>() -> <a href="./src/freeapiapp/types/chat_app/chat_list_response.py">ChatListResponse</a></code>

### Users

Types:

```python
from freeapiapp.types.chat_app.chats import UserListResponse
```

Methods:

- <code title="get /chat-app/chats/users">client.chat_app.chats.users.<a href="./src/freeapiapp/resources/chat_app/chats/users.py">list</a>() -> <a href="./src/freeapiapp/types/chat_app/chats/user_list_response.py">UserListResponse</a></code>

### C

Types:

```python
from freeapiapp.types.chat_app.chats import CCreateResponse
```

Methods:

- <code title="post /chat-app/chats/c/{receiverId}">client.chat_app.chats.c.<a href="./src/freeapiapp/resources/chat_app/chats/c.py">create</a>(receiver_id) -> <a href="./src/freeapiapp/types/chat_app/chats/c_create_response.py">CCreateResponse</a></code>

## Messages

Types:

```python
from freeapiapp.types.chat_app import MessageDeleteResponse
```

Methods:

- <code title="delete /chat-app/messages/{chatId}/{messageId}">client.chat_app.messages.<a href="./src/freeapiapp/resources/chat_app/messages.py">delete</a>(message_id, \*, chat_id) -> <a href="./src/freeapiapp/types/chat_app/message_delete_response.py">MessageDeleteResponse</a></code>

# Chats

Types:

```python
from freeapiapp.types import ChatRemoveResponse
```

Methods:

- <code title="delete /chat-app/chats/remove/{chatId}">client.chats.<a href="./src/freeapiapp/resources/chats/chats.py">remove</a>(chat_id) -> <a href="./src/freeapiapp/types/chat_remove_response.py">ChatRemoveResponse</a></code>

## Group

Types:

```python
from freeapiapp.types.chats import (
    GroupCreateResponse,
    GroupRetrieveResponse,
    GroupUpdateResponse,
    GroupDeleteResponse,
    GroupLeaveResponse,
    GroupParticipantAddResponse,
    GroupParticipantRemoveResponse,
)
```

Methods:

- <code title="post /chat-app/chats/group">client.chats.group.<a href="./src/freeapiapp/resources/chats/group.py">create</a>(\*\*<a href="src/freeapiapp/types/chats/group_create_params.py">params</a>) -> <a href="./src/freeapiapp/types/chats/group_create_response.py">GroupCreateResponse</a></code>
- <code title="get /chat-app/chats/group/{chatId}">client.chats.group.<a href="./src/freeapiapp/resources/chats/group.py">retrieve</a>(chat_id) -> <a href="./src/freeapiapp/types/chats/group_retrieve_response.py">GroupRetrieveResponse</a></code>
- <code title="patch /chat-app/chats/group/{chatId}">client.chats.group.<a href="./src/freeapiapp/resources/chats/group.py">update</a>(chat_id, \*\*<a href="src/freeapiapp/types/chats/group_update_params.py">params</a>) -> <a href="./src/freeapiapp/types/chats/group_update_response.py">GroupUpdateResponse</a></code>
- <code title="delete /chat-app/chats/group/{chatId}">client.chats.group.<a href="./src/freeapiapp/resources/chats/group.py">delete</a>(chat_id) -> <a href="./src/freeapiapp/types/chats/group_delete_response.py">GroupDeleteResponse</a></code>
- <code title="delete /chat-app/chats/leave/group/{chatId}">client.chats.group.<a href="./src/freeapiapp/resources/chats/group.py">leave</a>(chat_id) -> <a href="./src/freeapiapp/types/chats/group_leave_response.py">GroupLeaveResponse</a></code>
- <code title="post /chat-app/chats/group/{chatId}/{participantId}">client.chats.group.<a href="./src/freeapiapp/resources/chats/group.py">participant_add</a>(participant_id, \*, chat_id) -> <a href="./src/freeapiapp/types/chats/group_participant_add_response.py">GroupParticipantAddResponse</a></code>
- <code title="delete /chat-app/chats/group/{chatId}/{participantId}">client.chats.group.<a href="./src/freeapiapp/resources/chats/group.py">participant_remove</a>(participant_id, \*, chat_id) -> <a href="./src/freeapiapp/types/chats/group_participant_remove_response.py">GroupParticipantRemoveResponse</a></code>

# Messages

Types:

```python
from freeapiapp.types import MessageListResponse, MessageSendResponse
```

Methods:

- <code title="get /chat-app/messages/{chatId}">client.messages.<a href="./src/freeapiapp/resources/messages.py">list</a>(chat_id) -> <a href="./src/freeapiapp/types/message_list_response.py">MessageListResponse</a></code>
- <code title="post /chat-app/messages/{chatId}">client.messages.<a href="./src/freeapiapp/resources/messages.py">send</a>(chat_id, \*\*<a href="src/freeapiapp/types/message_send_params.py">params</a>) -> <a href="./src/freeapiapp/types/message_send_response.py">MessageSendResponse</a></code>

# Seed

## GeneratedCredentials

Types:

```python
from freeapiapp.types.seed import GeneratedCredentialListResponse
```

Methods:

- <code title="get /seed/generated-credentials">client.seed.generated_credentials.<a href="./src/freeapiapp/resources/seed/generated_credentials.py">list</a>() -> <a href="./src/freeapiapp/types/seed/generated_credential_list_response.py">GeneratedCredentialListResponse</a></code>

## Todos

Types:

```python
from freeapiapp.types.seed import TodoCreateResponse
```

Methods:

- <code title="post /seed/todos">client.seed.todos.<a href="./src/freeapiapp/resources/seed/todos.py">create</a>() -> <a href="./src/freeapiapp/types/seed/todo_create_response.py">TodoCreateResponse</a></code>

## Ecommerce

Types:

```python
from freeapiapp.types.seed import EcommerceCreateResponse
```

Methods:

- <code title="post /seed/ecommerce">client.seed.ecommerce.<a href="./src/freeapiapp/resources/seed/ecommerce.py">create</a>() -> <a href="./src/freeapiapp/types/seed/ecommerce_create_response.py">EcommerceCreateResponse</a></code>

## SocialMedia

Types:

```python
from freeapiapp.types.seed import SocialMediaCreateResponse
```

Methods:

- <code title="post /seed/social-media">client.seed.social_media.<a href="./src/freeapiapp/resources/seed/social_media.py">create</a>() -> <a href="./src/freeapiapp/types/seed/social_media_create_response.py">SocialMediaCreateResponse</a></code>

## ChatApp

Types:

```python
from freeapiapp.types.seed import ChatAppCreateResponse
```

Methods:

- <code title="post /seed/chat-app">client.seed.chat_app.<a href="./src/freeapiapp/resources/seed/chat_app.py">create</a>() -> <a href="./src/freeapiapp/types/seed/chat_app_create_response.py">ChatAppCreateResponse</a></code>

# ResetDB

Types:

```python
from freeapiapp.types import ResetDBDeleteResponse
```

Methods:

- <code title="delete /reset-db">client.reset_db.<a href="./src/freeapiapp/resources/reset_db.py">delete</a>() -> <a href="./src/freeapiapp/types/reset_db_delete_response.py">ResetDBDeleteResponse</a></code>

# Healthcheck

Types:

```python
from freeapiapp.types import HealthcheckRetrieveResponse
```

Methods:

- <code title="get /healthcheck">client.healthcheck.<a href="./src/freeapiapp/resources/healthcheck.py">retrieve</a>() -> <a href="./src/freeapiapp/types/healthcheck_retrieve_response.py">HealthcheckRetrieveResponse</a></code>
