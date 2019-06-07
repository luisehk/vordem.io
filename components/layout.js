import Head from 'next/head'
import Link from 'next/link'

const Layout = props => (
  <> 
    <Head>
      <title>Vordem | Digital Product Agency</title>
    	<meta
        name="viewport"
        content="width=device-width, initial-scale=1, shrink-to-fit=no" />
      <meta
        httpEquiv="X-UA-Compatible"
        content="ie=edge" />
      <link
        href="https://fonts.googleapis.com/css?family=PT+Sans:400,700"
        rel="stylesheet" />
      <link
        href="/static/css/index.css"
        rel="stylesheet" />

      <link
        rel="stylesheet"
        href="/static/css/reset.css" />
      <link
        rel="stylesheet"
        href="/static/css/index.css" />
      <link
        rel="stylesheet"
        href="/static/css/vordem.css" />

      <script
        type="text/javascript"
        src="https://code.jquery.com/jquery-3.3.1.min.js"></script>
      <script
        type="text/javascript"
        src="https://unpkg.com/masonry-layout@4/dist/masonry.pkgd.min.js"></script>
      <script
        src="/static/js/parsley.min.js"></script>

      <script
        async
        src="https://www.googletagmanager.com/gtag/js?id=UA-141127632-1"></script>

      <script dangerouslySetInnerHTML={{__html: `
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());

        gtag('config', 'UA-128121295-1');
      `}} />
    </Head>

    <header className="has-texture">
        <div className="wrap">
            <nav id="navbar" className="navbar column">
                <div className="container">
                    <div className="navbar-brand">
                        <Link href="/">
                          <a className="navbar-item">
                              <img src="/static/img/logo.svg" alt="Vordem" />
                          </a>
                        </Link>
                        <div id="navbarBurger" className="navbar-burger burger" data-target="navMenuDocumentation">
                            <span></span>
                            <span></span>
                            <span></span>
                        </div>
                    </div>
                    <div id="navMenuDocumentation" className="navbar-menu">
                        <div className="navbar-end">
                            <Link href="/">
                              <a className="navbar-item is-hidden-mobile txt18">Home</a>
                            </Link>
                            <Link href="/about">
                              <a className="navbar-item is-hidden-mobile txt18">What we do</a>
                            </Link>
                            <Link href="/work">
                              <a className="navbar-item is-hidden-mobile txt18">Our work</a>
                            </Link>
                            <Link href="/contact">
                              <a className="navbar-item is-hidden-mobile txt18">Contact us</a>
                            </Link>
                        </div>
                    </div>
                </div>
            </nav>
        </div>
    </header>

    <aside className="hero-nav is-hidden-desktop">
        <div className="hero-nav-close-wrap">
            <div className="hero-nav-close">
                <div></div>
                <div></div>
            </div>
        </div>
        <div className="one-col is-table">
            <div className="one-col is-table">
                <ul className="is-table-cell has-list has-text-centered" id="aside-menu">
                    <Link href="/">
                      <a className="c-white txt18 mb20 is-bold">Home</a>
                    </Link>
                    <Link href="/about">
                      <a className="c-white txt18 mb20 is-bold">What we do</a>
                    </Link>
                    <Link href="/work">
                      <a className="c-white txt18 mb20 is-bold">Our work</a>
                    </Link>
                    <Link href="/contact">
                      <a className="c-white txt18 mb20 is-bold">Contact us</a>
                    </Link>
                </ul>
            </div>
        </div>
    </aside>

    {props.children}

    <footer className="bg-red-gradient has-texture ptb40">
        <div className="wrap">
            <div className="columns">
                <div className="column is-one-quarter"><img src="/static/img/logo.svg" alt="Vordem" /></div>
                <div className="column is-half">
                    <div className="columns is-mobile">
                        <div className="column is-half has-list">
                            <p className="bd-footer-link">
                              <Link href="/">
                                <a className="txt18">Home</a>
                              </Link>
                            </p>
                            <p className="bd-footer-link">
                              <Link href="/about">
                                <a className="txt18">What we do</a>
                              </Link>
                            </p>
                        </div>
                        <div className="column is-half has-list">
                            <p className="bd-footer-link">
                              <Link href="/work">
                                <a className="txt18">Our work</a>
                              </Link>
                            </p>
                            <p className="bd-footer-link">
                              <Link href="/contact">
                                <a className="txt18">Contact us</a>
                              </Link>
                            </p>
                        </div>
                    </div>
                </div>
                <div className="column is-flex-tablet is-one-quarter">
                    <Link href="/contact">
                      <a className="button bg-white c-red has-arrow is-right">Request Quote</a>
                    </Link>
                </div>
            </div>
        </div>
    </footer>

    <script
      type="text/javascript"
      src="/static/js/scripts.js"></script>
    <script
      type="text/javascript"
      src="/static/js/vordem.js"></script>

  </>
)

export default Layout