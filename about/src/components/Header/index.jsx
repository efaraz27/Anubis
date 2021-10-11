import React from 'react';
import Nav from './Nav';

const Header = () => {
  return (
    <div className='w-full flex flex-row justify-between pt-lg pb-lg'>
      <div>
        Anubis
      </div>
      <Nav />


    </div>
  )
}

export default Header;
