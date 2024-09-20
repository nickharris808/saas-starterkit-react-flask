import React, { useState } from 'react';
import Navigation from './Navigation';

const Dashboard = () => {
  const [activeTab, setActiveTab] = useState('tab1');

  const handleTabChange = (tab) => {
    setActiveTab(tab);
  };

  return (
    <div className="min-h-screen bg-gray-100">
      <Navigation />
      <div className="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
        <h1 className="text-3xl font-bold text-gray-900 mb-6">Dashboard</h1>
        <div className="bg-white shadow-sm rounded-lg overflow-hidden">
          <div className="border-b border-gray-200">
            <nav className="-mb-px flex">
              <button
                onClick={() => handleTabChange('tab1')}
                className={`w-1/3 py-4 px-1 text-center border-b-2 font-medium text-sm ${
                  activeTab === 'tab1'
                    ? 'border-indigo-500 text-indigo-600'
                    : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300'
                }`}
              >
                Tab 1
              </button>
              <button
                onClick={() => handleTabChange('tab2')}
                className={`w-1/3 py-4 px-1 text-center border-b-2 font-medium text-sm ${
                  activeTab === 'tab2'
                    ? 'border-indigo-500 text-indigo-600'
                    : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300'
                }`}
              >
                Tab 2
              </button>
              <button
                onClick={() => handleTabChange('tab3')}
                className={`w-1/3 py-4 px-1 text-center border-b-2 font-medium text-sm ${
                  activeTab === 'tab3'
                    ? 'border-indigo-500 text-indigo-600'
                    : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300'
                }`}
              >
                Tab 3
              </button>
            </nav>
          </div>
          <div className="p-4">
            {activeTab === 'tab1' && (
              <div>
                <h2 className="text-lg font-semibold mb-2">Tab 1 Content</h2>
                <p>This is the content for Tab 1.</p>
              </div>
            )}
            {activeTab === 'tab2' && (
              <div>
                <h2 className="text-lg font-semibold mb-2">Tab 2 Content</h2>
                <p>This is the content for Tab 2.</p>
              </div>
            )}
            {activeTab === 'tab3' && (
              <div>
                <h2 className="text-lg font-semibold mb-2">Tab 3 Content</h2>
                <p>This is the content for Tab 3.</p>
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;