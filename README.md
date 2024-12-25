# Kleo: Lightweight Experimental Blockchain  

**Kleo** is a lightweight blockchain designed to demonstrate the fundamental principles of blockchain technology. It features a clean user interface and persistent storage powered by MongoDB, making it easy to explore the concepts of distributed ledgers and cryptographic hashing.  

## Features  

1. **Blockchain Fundamentals**  
   - A **Block** class that encapsulates: 
     - **index**: Index of the block
     - **Data**: Transaction or information stored in the block.  
     - **Previous Hash**: Reference to the previous block in the chain.  
     - **Timestamp**: Time the block was created.  
     - **Current Hash**: Unique identifier generated using SHA-256.  
   - A **Blockchain** class that manages the chain and ensures its integrity.  

2. **Key Functionalities**  
   - **Genesis Block Creation**: Automatically generates the first block in the chain.  
   - **Add Block**: Appends new blocks to the chain, linking them via hashes.  
   - **Validation**: Ensures the integrity of the blockchain by verifying each block.  
   - **Persistence**: Stores and retrieves blockchain data using MongoDB.  

3. **Frontend Client**  
   - User-friendly interface for creating and viewing transactions.  
   - Interacts with the blockchain backend to simulate a decentralized ledger.  

## Architecture  

### Block Class  
Handles individual blocks in the blockchain.  
- **Attributes**:
  - `index`: Index of the block
  - `data`: Payload for the block.  
  - `previousHash`: Hash of the previous block in the chain.  
  - `timestamp`: Block creation timestamp.  
  - `currentHash`: Generated using the `calculateHash` method.  
- **Methods**:  
  - `calculateHash`: Combines the block's index, data, timestamp, and previous hash, then hashes them using SHA-256.  

### Blockchain Class  
Manages the overall blockchain.  
- **Attributes**:  
  - `chain`: Array of blocks.  
  - `dbConnection`: MongoDB connection for persistence.  
  - `loadFromDatabase`: Loads blockchain data from MongoDB.  
- **Methods**:  
  - `createGenesisBlock`: Initializes the blockchain with the first block.  
  - `addBlock`: Adds a new block to the chain.  
  - `saveToDatabase`: Saves the blockchain to MongoDB.  
  - `displayBlockchain`: Prints the chain for debugging or analysis.  
  - `blockchainSize`: Returns the number of blocks in the chain.  
  - `getBlockchain`: Fetches the entire chain.  
  - `validateBlockchain`: Ensures the chain's validity by verifying each block.  

### MongoDB Integration  
- Stores blockchain data persistently.  
- Ensures data is not lost between application restarts.  

### Frontend Client  
- A simple interface for:  
  - Submitting transactions.  
  - Viewing the blockchain.  
  - Visualizing the linkage between blocks through their hashes.  

## How It Works  

1. The **Genesis Block** is automatically created when the blockchain is initialized.  
2. Users can add transactions via the frontend, which creates new blocks.  
3. Each new block references the hash of the previous block, ensuring immutability.  
4. Blockchain data is stored in MongoDB for persistence and loaded when the application starts.  
5. The chain can be validated at any time to ensure its integrity.  

## Getting Started  

### Prerequisites
- Python 3.10.12
- nodeJS v20.18.0
- MongoDB  

### Installation  
1. Clone the repository:  
   ```bash  
   git clone https://github.com/3akare/Kleo
   cd Kleo
   ```  
2. Install dependencies:  
   ```bash 
   cd server
   pip install -r requirement.txt  
   
   cd ../client
   npm install
   ```  
3. Start MongoDB:  
   ```bash  
   mongod  
   ```  
4. Run the application:  
   ```bash  
   cd ../client
   npm run dev
   
   cd ../server
   python3 main.py
   ```  

### Using the Client  
1. Open the frontend in your browser.  
2. Submit transactions to add new blocks.  
3. View the updated blockchain.  


## Contributing  

Contributions are welcome! Submit a pull request or report issues in the GitHub repository.  

## License  

This project is licensed under the MIT License.
