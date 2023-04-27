<template>
    <div>
      <h2>Import Transactions</h2>
      <form @submit.prevent="importCsv">
        <div class="form-group">
          <label for="csvFile">Select CSV File</label>
          <input type="file" class="form-control" id="csvFile" ref="csvFile" accept=".csv"/>
        </div>
        <button type="submit" class="btn btn-primary">Import</button>
      </form>
    </div>
    <div>
      <button class="btn btn-danger mt-3" @click="deleteAllTransactions">Delete all transactions</button>
    </div>
    <div>
      <button class="btn btn-success mt-3" @click="exportAllTransactions">Export all transactions</button>
      <a ref="csvDownloadLink" style="display: none;"></a>
    </div>

  </template>

  <script>

  import axios from "axios";
  import Papa from "papaparse";

  const hostUrl = "http://127.0.0.1:8000";

  export default {

    data() {
        return {
            importedTransactions: [],
        }
    },

    methods: {

      // ===================  EXPORT TO CSV ==============================

      async exportAllTransactions() {
        try {
          const transactions = await this.getAllTransactions();
          const csvContent = this.convertTransactionsToCsv(transactions);
          this.downloadCsv(csvContent);
        } catch (error) {
          console.error("Error exporting transactions:", error);
        }
      },

      async getAllTransactions() {
        try {
          const response = await axios.get(`${hostUrl}/transaction/`);
          return response.data;
        } catch (error) {
          console.error("Error getting transactions:", error);
          return [];
        }
      },

      convertTransactionsToCsv(transactions) {
        const header = ["date", "type", "amount", "description", "category"];
        const csvData = transactions.map((transaction) => [
          transaction.date,
          transaction.type,
          transaction.amount,
          transaction.description,
          transaction.category,
        ]);
        csvData.unshift(header);
        return Papa.unparse(csvData);
      },

      downloadCsv(csvContent) {
        const blob = new Blob([csvContent], { type: "text/csv;charset=utf-8" });
        const url = URL.createObjectURL(blob);

        const downloadLink = this.$refs.csvDownloadLink;
        downloadLink.href = url;
        downloadLink.download = "transactions.csv";
        downloadLink.click();
        URL.revokeObjectURL(url);
      },

// ===================  IMPORT FROM CSV ==============================

      async importCsv() {

        // console.log('import called');

        const file = this.$refs.csvFile.files[0];
        if (!file) {
          alert("Please select file for import");
          return;
        }

        let readTransactionsCount = 0;

        Papa.parse(file, {
          header: true,
          skipEmptyLines: true,
          complete: (results) => {
            this.importedTransactions = results.data;
            readTransactionsCount = this.importedTransactions.length;
            this.processTransactions(this.importedTransactions);
            alert(`${readTransactionsCount} transactions imported successfully.`)
          },
        });

        // Make sure we have imported same number of transactions as read from CSV file
        // const totalSavedTransactions = await this.getTransactionsCount();
        // if (readTransactionsCount === totalSavedTransactions){
        //   alert(`All ${readTransactionsCount} transactions imported successfully.`)
        // } else {

          //   const error_text = `Error: ${readTransactionsCount} transactions read from CSV file, but ${totalSavedTransactions} imported successfully.`;
          //   console.error(error_text);
          //   alert(error_text);
          // }

      },

      processTransactions(transactions) {
        transactions.forEach((transaction) => {
          this.createTransaction(transaction);
        });
      },

      createTransaction(transactionData) {
        const newTransaction = {
          date: transactionData.date,
          type: transactionData.type,
          amount: transactionData.amount,
          description: transactionData.description,
          category: transactionData.category,
        };

        axios.post(`${hostUrl}/transaction/`, newTransaction)
            .catch((error) => {
                console.error(`Error creating transaction: ${newTransaction}`, error);
            });
      },

      // =================== DELETE ALL TRANSACTIONS ==============================

      async deleteAllTransactions() {
      const totalTransactions = await this.getTransactionsCount();
      if (
        confirm(
          `Do you really want to delete data for all ${totalTransactions} transactions?`
        )
      ) {
        axios
          .delete(`${hostUrl}/transaction/delete_all/`)
          .then(() => {
            alert("All transactions have been deleted.");
          })
          .catch((error) => {
            console.error("Error deleting all transactions:", error);
          });
      }
    },

    async getTransactionsCount() {
      try {
        const response = await axios.get(`${hostUrl}/transaction/`);
        return response.data.length;
      } catch (error) {
        console.error("Error getting transactions count:", error);
        return 0;
      }
    },


    },
  };
  </script>
