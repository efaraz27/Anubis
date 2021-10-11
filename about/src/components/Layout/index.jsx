import React from 'react';

import Header from '../Header';
import Footer from '../Footer';
// import GetStartedModal from '../GetStartedModal';

const Layout = ({ children }) => {
  return (
      <div>
        <Header />
        <main>{children}</main>
        <Footer />
        {/*<GetStartedModal />*/}
      </div>
  )
}

export default Layout;