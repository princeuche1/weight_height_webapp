mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"prince.uche@e4email.net\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml
